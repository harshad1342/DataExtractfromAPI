document.getElementById('searchButtonFacebook').addEventListener('click', function() {
    var query = document.getElementById('searchInput').value;
    var duration = document.getElementById('durationSelect').value;
    // Redirect to Facebook search page with the selected duration
    window.location.href = "/facebook_search/" + query;
  });