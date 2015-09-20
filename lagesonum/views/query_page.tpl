% include('views/header.tpl', active='query')

<div class="container">
      <div class="starter-template">

<p>{{_('search_pitch')}}</p>


<form action="{{i18n_path('/query')}}" method="post" class="form-inline" style="margin-bottom:20px;">
  <div class="form-group">
    <label for="numberfield">Your Number:</label>
    <input type="text" name="number" class="form-control" placeholder="e.g. A123" id="numberfield">
  </div>
  <button class="btn btn-primary">{{_('submit_label')}}</button>
</form>



% if result is not None:
  %if invalid_input:
    <div class="alert alert-warning" role="alert"><code>{{invalid_input}}</code> is not a valid number!</div>
  %else:
    %if len(timestamps) == 0:
      <div class="alert alert-warning" role="alert">Your number was not found.</div>
    % else:
      <div class="alert alert-success" role="alert">
        Your number <b>{{result}}</b> was found!<br><br>

        % if len(timestamps) == 1:
          it was seen on <b>{{timestamps[0]}}</b>
        % else:
          it was seen <b>{{len(timestamps)}}</b> times: {{", ".join(timestamps)}}
        % end
      </div>
    % end
  %end
% end


<h3>{{_('pleasenote_title')}}</h3>
<p>{{_('pleasenote')}}</p>

</div></div>

% include('views/footer.tpl')


