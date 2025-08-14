from django.conf import settings
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend suitable for server environments
import matplotlib.pyplot as plt

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomSignupForm
import numpy as np
import rasterio
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from matplotlib.colors import ListedColormap
# from django.conf import settings
# import matplotlib.pyplot as plt
import os
from tensorflow.keras.models import load_model

model_path = os.path.join(settings.BASE_DIR, 'static', 'forest_UNET.h5')
cnn_model = load_model(model_path)

def main(request):
    return render(request, 'main.html')

@login_required(login_url='auth')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='auth')
def results(request):
    return render(request, 'results.html')

@login_required(login_url='auth')
def report(request):
    return render(request, 'report.html')

@login_required(login_url='auth')
def predict(request):
    return render(request, 'predict.html')

@login_required(login_url='auth')
def forest(request):
    return render(request, 'forest.html')

@login_required(login_url='auth')
def change(request):
    return render(request, 'change.html')

@login_required(login_url='auth')
def dataset(request):
    return render(request, 'dataset.html')


def calculate_indices_anjaneri(image_path):
    with rasterio.open(image_path) as src:
        red = src.read(3).astype(np.float32)     # Band 4
        nir = src.read(7).astype(np.float32)     # Band 8
        normalized = src.read(1).astype(np.float32)
        scl = src.read(10)
        ndvi = (nir - red) / (nir + red + 1e-5)
        return ndvi, normalized, scl, src.meta

def calculate_indices_igatpuri(image_path):
    with rasterio.open(image_path) as src:
        green = src.read(3).astype(np.float32)   # Band 3
        red = src.read(4).astype(np.float32)     # Band 4
        nir = src.read(8).astype(np.float32)     # Band 8
        normalized = src.read(1).astype(np.float32)
        scl = src.read(10)                       # Scene Classification Layer
        ndvi = (nir - red) / (nir + red + 1e-5)
        ndwi = (green - nir) / (green + nir + 1e-5)
        return ndvi, ndwi, normalized, scl, src.meta
@login_required(login_url='auth')
def analyze_changes(request):
    if request.method == 'POST':
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        date1 = request.POST['date1']
        date2 = request.POST['date2']
        location = request.POST.get('location', '').strip().lower()
        year_range = f"{date1}–{date2}"

        # Save uploaded images
        img1_path = default_storage.save(f"uploads/{image1.name}", image1)
        img2_path = default_storage.save(f"uploads/{image2.name}", image2)
        img1_path = os.path.join(settings.MEDIA_ROOT, img1_path)
        img2_path = os.path.join(settings.MEDIA_ROOT, img2_path)

        # Extract indices based on location
        if "igatpuri" in location:
            ndvi1, ndwi1, norm1, scl1, meta1 = calculate_indices_igatpuri(img1_path)
            ndvi2, ndwi2, norm2, scl2, meta2 = calculate_indices_igatpuri(img2_path)
        else:  # default Anjaneri or others
            ndvi1, norm1, scl1,meta1 = calculate_indices_anjaneri(img1_path)
            ndvi2, norm2, scl1, meta2 = calculate_indices_anjaneri(img2_path)
            ndwi1 = ndwi2 = None
            scl1 = scl2 = None

        if ndvi1.shape != ndvi2.shape:
            return render(request, "error.html", {"error": "Images must have the same dimensions"})

        # NDVI difference
        ndvi_diff = ndvi2 - ndvi1
        change_matrix = np.zeros_like(ndvi1, dtype=np.uint8)

        # Use dynamic thresholds
        if "igatpuri" in location:
            gain_thresh, loss_thresh = 0.05, -0.05
        else:  # Anjaneri or others
            gain_thresh, loss_thresh = 0.14, -0.14

        # Apply NDVI thresholds
        change_matrix[ndvi_diff > gain_thresh] = 2  # Gain
        change_matrix[ndvi_diff < loss_thresh] = 1  # Loss

        # Handle ignored areas and shadows only if scl available
        if scl1 is not None:
            shadow_mask = np.isin(scl1, [3, 8, 9, 10])
        else:
            shadow_mask = np.zeros_like(change_matrix, dtype=bool)

        ignored_mask = (norm1 == 0.0) & (norm2 == 0.0)
        change_matrix[shadow_mask | ignored_mask] = 255

        # Optional water detection for Igatpuri
        if "igatpuri" in location and ndwi1 is not None:
            water_mask = ndwi1 > 0
            change_matrix[water_mask] = 3

        # Area calculation (assuming 10m x 10m pixels = 0.0001 sq km)
        pixel_area_km2 = 0.0001
        gain_area = np.sum(change_matrix == 2) * pixel_area_km2
        loss_area = np.sum(change_matrix == 1) * pixel_area_km2
        water_area = np.sum(change_matrix == 3) * pixel_area_km2 if "igatpuri" in location else 0
        no_change_area = np.sum(change_matrix == 0) * pixel_area_km2

        # Save TIF result
        output_filename = f"change_result_{date1}_{date2}.tif"
        output_path = os.path.join(settings.MEDIA_ROOT, "results", output_filename)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        meta1.update({"count": 1, "dtype": 'uint8'})

        with rasterio.open(output_path, "w", **meta1) as dst:
            dst.write(change_matrix, 1)

        # Step : Construct NDVI input image URLs
        heatmap_base_url = f"Heatmap Visualization Data/{location.capitalize()}"
        ndvi_image1_url = f"{settings.STATIC_URL}{heatmap_base_url}/{location.capitalize()}-{date1}.png"
        ndvi_image2_url = f"{settings.STATIC_URL}{heatmap_base_url}/{location.capitalize()}-{date2}.png"


        # Save visualization
        visual_filename = f"visual_{date1}_{date2}.png"
        visual_path = os.path.join(settings.MEDIA_ROOT, "results", visual_filename)
        plt.figure(figsize=(6, 6))
        masked = np.ma.masked_where(change_matrix == 255, change_matrix)

        # Colormap with optional water
        if "igatpuri" in location:
            cmap = ListedColormap(["gray", "red", "green", "blue"])  # No Change, Loss, Gain, Water
            ticks = [0, 1, 2, 3]
            labels = ["No Change", "Loss", "Gain", "Water"]
        else:
            cmap = ListedColormap(["gray", "red", "green"])  # No Change, Loss, Gain
            ticks = [0, 1, 2]
            labels = ["No Change", "Loss", "Gain"]

        plt.imshow(masked, cmap=cmap)
        plt.axis('off')
        cbar = plt.colorbar(ticks=ticks, label="Change Class")
        cbar.ax.set_yticklabels(labels)
        plt.savefig(visual_path, bbox_inches='tight')
        plt.close()



        context = {
            "gain_area": f"{gain_area:.2f}",
            "loss_area": f"{loss_area:.2f}",
            "no_change_area": f"{no_change_area:.2f}",
            "location": location.capitalize(),
            "visual_url": settings.MEDIA_URL + "results/" + os.path.basename(visual_path),
            "tif_url": settings.MEDIA_URL + f"results/{output_filename}",
            "year_range": year_range,
            "ndvi_image1_url": ndvi_image1_url,
            "ndvi_image2_url": ndvi_image2_url,
            "earlier_year": date1,
            "later_year": date2,
        }

        if "igatpuri" in location:
            context["water_area"] = f"{water_area:.2f}"

        return render(request, "analyze_changes.html", context)

    else:
        return render(request, "change.html")




def auth(request):
    login_form = AuthenticationForm()
    signup_form = CustomSignupForm()
    active_form = 'login'

    if request.method == 'POST':
        if 'login_submit' in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            active_form = 'login'
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                return redirect('main')  # your main app page after login
        elif 'signup_submit' in request.POST:
            signup_form = CustomSignupForm(request.POST)
            active_form = 'signup'
            if signup_form.is_valid():
                signup_form.save()
                # Redirect to auth page to show login form after signup
                return redirect('auth')

    context = {
        'login_form': login_form,
        'signup_form': signup_form,
        'active_form': active_form,
    }
    return render(request, 'signup.html', context)

def logout_view(request):
    auth_logout(request)
    return redirect('main')