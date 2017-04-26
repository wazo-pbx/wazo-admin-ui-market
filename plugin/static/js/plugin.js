$(document).on('click', "[data-installed]", function() {
    is_installed = $(this).attr("data-installed");
    name = $(this).attr("data-name");
    url = $(this).attr("data-url");
    namespace = $(this).attr("data-namespace");
    method = $(this).attr("data-method");

    body = {
      namespace: namespace,
      name: name,
      url: url,
      method: method
    }

    if (is_installed == 'True') {
      remove_url = $(this).attr("data-remove-url");
      remove_plugin(remove_url, body);
    } else {
      install_url = $(this).attr("data-install-url");
      install_plugin(install_url, body);
    }
});

$('#search_plugin').on('change', function() {
    res = $('#search_plugin').val();
    search_url = $('#search_plugin').attr("data-search-url");

    if (res) {
      search = {
        value: res
      }
      call_ajax_plugin(search_url, search, callback_search);
    }
});

$('#filter_plugin').on('change', function() {
    res = $('#filter_plugin').val();
    filter_url = $('#filter_plugin').attr("data-filter-url");

    if (res) {
      filter = {
        value: res
      }
      call_ajax_plugin(filter_url, filter, callback_filter);
    }
});

function remove_plugin(remove_url, body) {
  res = confirm('Are you sure you want to remove this plugin?');
  if (res == true) {
    launch_remove_plugin(remove_url, body);
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
  call_ajax_plugin(install_url, body, callback_install);
}

function launch_remove_plugin(remove_url, body) {
  $('#' + body.name).removeClass('hidden');
  call_ajax_plugin(remove_url, body, callback_remove);
}

function callback_install(data) {
  $('#' + body.name).addClass('hidden');
  console.log(data);
}

function callback_remove(data) {
  $('#' + body.name).addClass('hidden');
  console.log(data);
}

function callback_search(data) {
  console.log(data);
}

function callback_filter(data) {
  console.log(data);
}

function call_ajax_plugin(url, body, callback) {
  $.ajax({
    url: url,
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(body),
    success: function(data) {
      callback(data);
    }
  });
}
