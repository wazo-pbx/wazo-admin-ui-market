var socket = null;
var started = false;
var btn_loading = null;

$(document).ready(function() {
    btn_loading = Ladda.create(document.querySelector('.ladda-button'));
    show_only_official();
});

function connect(token) {
    if (socket != null) {
        console.log("socket already connected");
        return;
    }

    var host = window.location.host;
    var ws_url = "wss://" + host + "/api/websocketd/?token=" + token;
    socket = new WebSocket(ws_url);
    socket.onclose = function(event) {
        socket = null;
        console.log("websocketd closed with code " + event.code + " and reason '" + event.reason + "'");
    };
    socket.onmessage = function(event) {
        if (started) {
            var payload = JSON.parse(event.data);
            if (payload.data.status == 'completed') {
                console.log('Time to reload webi');
                location.reload();
            }
            return;
        }

        var msg = JSON.parse(event.data);
        switch (msg.op) {
            case "init":
                subscribe("plugin_install_progress");
                subscribe("plugin_uninstall_progress");
                start();
                break;
            case "start":
                started = true;
                console.log("waiting for messages");
                break;
        }
    };
    started = false;
}

function subscribe(event_name) {
    var msg = {
        op: "subscribe",
        data: {
          event_name: event_name
        }
    };
    socket.send(JSON.stringify(msg));
};

function start() {
    var msg = {
        op: "start"
    };
    socket.send(JSON.stringify(msg));
}

$(document).on('click', "[data-installed]", function() {
    is_installed = $(this).attr("data-installed");
    name = $(this).attr("data-name");
    url = $(this).attr("data-url");
    namespace = $(this).attr("data-namespace");
    method = $(this).attr("data-method");
    options = $(this).attr("data-options") || '{}';
    options = $.parseJSON(options);

    body = {
      namespace: namespace,
      name: name,
      url: url,
      method: method,
      options: options
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
    url = $('#git-url-to-install').val();
    if (url) {
      body = {
        url: url,
        method: 'git'
      }

      install_url = $(this).attr("data-install-url");
      install_plugin(install_url, body, from_git=true);
    }
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
    filter_plugins();
});

$('#show_only_official').on('change', function() {
  show_only_official();
});

function show_only_official() {
  filter_url = $('#show_only_official').attr("data-show-official-url");
  official = $('#show_only_official').is(':checked');
  if (official) {
    call_ajax_plugin(filter_url, callback_filter);
  } else {
    filter_plugins();
  }
}

function filter_plugins() {
  res = $('#filter_plugin').val();
  filter_url = $('#filter_plugin').attr("data-filter-url");
  if (res) {
    filter = {
      value: res
    }
  }
  call_ajax_plugin(filter_url, callback_filter, filter);
}

function remove_plugin(remove_url, body) {
  res = confirm('Are you sure you want to remove this plugin?');
  if (res == true) {
    launch_remove_plugin(remove_url, body);
  }
}

function install_plugin(install_url, body, from_git=false) {
  res = confirm('Are you sure you want to install this plugin?');
  if (res == true) {
    if (from_git) {
      btn_loading.start();
    }
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
}

function callback_remove(data) {
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
        console.log('There is some error, please reload');
        location.reload();
      }, 4000);
    }
  });
}
