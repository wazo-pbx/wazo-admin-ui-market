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

$(document).on('click', "[data-git-install]", function() {
    body = {
      url: $('#git-url-to-install').val(),
      method: 'git'
    }
    install_url = $(this).attr("data-install-url");
    install_plugin(install_url, body);
});

$('#search_plugin').on('change', function() {
    res = $('#search_plugin').val();
    search_url = $('#search_plugin').attr("data-search-url");

    if (res) {
      search = {
        value: res
      }
      call_ajax_plugin(search_url, callback_search, search);
    }
});

$('#filter_plugin').on('change', function() {
    res = $('#filter_plugin').val();
    filter_url = $('#filter_plugin').attr("data-filter-url");

    if (res) {
      filter = {
        value: res
      }
      call_ajax_plugin(filter_url, callback_filter, filter);
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
  call_ajax_plugin(install_url, callback_install, body);
}

function launch_remove_plugin(remove_url, body) {
  $('#' + body.name).removeClass('hidden');
  call_ajax_plugin(remove_url, callback_remove, body);
}

function callback_install(data) {
  $('#' + body.name).addClass('hidden');
  location.reload();
}

function callback_remove(data) {
  $('#' + body.name).addClass('hidden');
  location.reload();
}

function callback_search(data) {
  $('#plugins').html(data);
}

function callback_filter(data) {
  $('#plugins').html(data);
}

function callback_list(data) {
  $('#plugins').html(data);
}

function call_ajax_plugin(url, callback, body, method) {
  if (!method) { method = 'POST'; }
  if (body == '') { data = null; } else { data = JSON.stringify(body); }
  $.ajax({
    url: url,
    type: method,
    contentType: 'application/json',
    data: data,
    success: function(data) {
      callback(data);
    },
    error: function(data) {
      setTimeout(function() {
        location.reload();
      }, 3000);
    }
  });
}
