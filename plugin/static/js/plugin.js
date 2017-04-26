$(document).on('click', "[data-installed]", function() {
    is_installed = $(this).attr("data-installed");
    name = $(this).attr("data-name");
    url = $(this).attr("data-url");
    namespace = $(this).attr("data-namespace");
    method = $(this).attr("data-method");
    install_url = $(this).attr("data-install-url");

    body = {
      namespace: namespace,
      name: name,
      url: url,
      method: method
    }

    if (is_installed == 'True') {
      remove_plugin(body);
    } else {
      install_plugin(install_url, body);
    }
});

function remove_plugin(body) {
  res = confirm('Are you sure you want to remove this plugin?');
  if (res == true) {
    launch_remove_plugin(body);
  }
}

function install_plugin(install_url, body) {
  res = confirm('Are you sure you want to install this plugin?');
  if (res == true) {
    launch_install_plugin(install_url, body);
  }
}

function launch_install_plugin(install_url, body) {
  $('#' + body.name).removeClass('hidden');
  call_install_plugin(install_url, body);
}

function launch_remove_plugin(body) {
  $('#' + body.name).removeClass('hidden');
  setTimeout(function() {
    $('#' + body.name).addClass('hidden');
  }, 3000);
}

function call_install_plugin(install_url, body) {
  $.ajax({
    url: install_url,
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(body),
    success: function(data) {
      $('#' + body.name).addClass('hidden');
      console.log(data);
    }
  });
}
