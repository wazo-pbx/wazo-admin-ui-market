$(document).on('click', "[data-installed]", function() {
    is_installed = $(this).attr("data-installed");
    name = $(this).attr("data-name");
    url = $(this).attr("data-url");

    if (is_installed == 'True') {
      remove_plugin(name);
    } else {
      install_plugin(name, url);
    }
});

function remove_plugin(name) {
  res = confirm('Are you sure you want to remove this plugin?');
  if (res == true) {
    launch_remove_plugin(name);
  }
}

function install_plugin(name, url) {
  res = confirm('Are you sure you want to install this plugin?');
  if (res == true) {
    launch_install_plugin(name, url);
  }
}

function launch_install_plugin(name, url) {
  $('#' + name).removeClass('hidden');
  setTimeout(function() {
    $('#' + name).addClass('hidden');
  }, 5000);
}

function launch_remove_plugin(name) {
  $('#' + name).removeClass('hidden');
  setTimeout(function() {
    $('#' + name).addClass('hidden');
  }, 3000);
}
