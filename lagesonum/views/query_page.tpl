% include('views/header.tpl', active='query')

<div class="container">
      <div class="starter-template">

<p>{{_('search_pitch')}}</p>


<form action="{{i18n_path('/query')}}" method="post" class="form-inline" style="margin-bottom:20px;">
  <div class="form-group">
    <label for="numberfield">{{_('txtnumber')}}</label>
    <input type="text" name="number" class="form-control" placeholder="{{_('inputexample')}}" id="numberfield">
  </div>
  <button class="btn btn-primary">{{_('submit_label')}}</button>
</form>

<h3>{{_(u'numberorigin_head')}}</h3>
<p>{{_(u'numberorigin_xplain')}}</p>
<a href="enter">{{_(u'help entering numbers')}}</a>

% if result is not None and result!="NewNumber":
  %if invalid_input:
    <div class="alert alert-warning" role="alert">{{_(u'errinvalinput')}}</div>
  %else:
    %if len(timestamps) == 0:
      <div class="alert alert-warning" role="alert">{{_('errnotfound')}}</div>
    % else:
      <div class="alert alert-success" role="alert">
        {{_('querysuccess') % ({'number': result})}}<br><br>

        % if len(timestamps) == 1:
           {{_('foundonce') % ({'date': timestamps})}} <br><br>
        % else:
           {{_('foundmultiple') % ({'amount': len(timestamps), 'date': timestamps})}}
        % end

        {{_('morelikely')}}
      </div>
    % end
  %end



<h3>{{_('pleasenote_title')}}</h3>
<p>{{_(u'pleasenote')}}</p>

</div></div>

% include('views/footer.tpl')


