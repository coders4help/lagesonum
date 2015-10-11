% include('views/header.tpl', active='helpus')


<div class="container">
      <div class="starter-template">

<p>{{_(u'help_pitch')}}</p>

<div>
<form action="{{i18n_path(request.fullpath)}}" method="post">
  <div class="form-group">
    <textarea name="numbers" rows="10" class="form-control" placeholder="{{_('inputexample')}}"></textarea>
  </div>
  <button class="btn btn-primary">{{_('submit_label')}}</button>
</form>
</div>

% if entered:
<div class="para">
{{_('entered')}} [{{locale_datetime(timestamp).translate(locale_translate)}}]:
<ul>
% for number in entered:
    <li><b>{{number}}</b></li>
% end
</ul>
</div>
%end

% if nonunique:
<div class="para">
{{_('erruniquenumber')}}:
<ul>
%for number in nonunique:
    <li><b>{{number}}</b></li>
%end
</ul>
</div>
%end

% if failed:
<div class="para">
Die folgenden Nummern sind offenbar ungültig und konnten nicht gespeichert werden:
<ul>
% for number in failed:
    <li><b>{{number}}</b></li>
% end
</ul>
</div>
%end
</div>
</div>

% include('views/footer.tpl')
