////// File upload feedback
////document.addEventListener("DOMContentLoaded", function () {
////    const file1 = document.getElementById('file1');
////    const file2 = document.getElementById('file2');
////    const file1Status = document.getElementById('file1-status');
////    const file2Status = document.getElementById('file2-status');
////    const form = document.getElementById('uploadForm');
////
////    file1.addEventListener('change', function (e) {
////        file1Status.style.display = 'block';
////        file1Status.textContent = 'Selected: ' + e.target.files[0].name;
////    });
////
////    file2.addEventListener('change', function (e) {
////        file2Status.style.display = 'block';
////        file2Status.textContent = 'Selected: ' + e.target.files[0].name;
////    });
////
////    form.addEventListener('submit', function (e) {
////        e.preventDefault(); // Prevent actual submission
////        // Simulate processing or integrate with backend
////        window.location.href = 'analyze_changes.html'; // Redirect to results page
////    });
////});
//
//
//// File upload feedback
//document.addEventListener("DOMContentLoaded", function () {
//    const file1 = document.getElementById('file1');
//    const file2 = document.getElementById('file2');
//    const file1Status = document.getElementById('file1-status');
//    const file2Status = document.getElementById('file2-status');
//
//    file1.addEventListener('change', function (e) {
//        file1Status.style.display = 'block';
//        file1Status.textContent = 'Selected: ' + e.target.files[0].name;
//    });
//
//    file2.addEventListener('change', function (e) {
//        file2Status.style.display = 'block';
//        file2Status.textContent = 'Selected: ' + e.target.files[0].name;
//    });
//
//    // No need to prevent form submission — let Django handle it
//});


document.addEventListener("DOMContentLoaded", function () {
    const file1 = document.getElementById('file1');
    const file2 = document.getElementById('file2');
    const file1Status = document.getElementById('file1-status');
    const file2Status = document.getElementById('file2-status');

    file1.addEventListener('change', function (e) {
        file1Status.style.display = 'block';
        file1Status.textContent = 'Selected: ' + e.target.files[0].name;
    });

    file2.addEventListener('change', function (e) {
        file2Status.style.display = 'block';
        file2Status.textContent = 'Selected: ' + e.target.files[0].name;
    });

    // ❌ DO NOT prevent form submission
    // ✅ Let Django handle the submission and response
});
