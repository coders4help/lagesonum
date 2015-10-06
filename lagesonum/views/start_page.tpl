% include('views/header.tpl', active='helpus')


<div class="container">
      <div class="starter-template">

<p>{{_(u'help_pitch')}}</p>

<form action="{{i18n_path(get('path', '/enter'))}}" method="post">
  <div class="form-group">
    <textarea name="numbers" rows="10" class="form-control" placeholder="{{_('inputexample')}}"></textarea>
  </div>
  <button class="btn btn-primary">{{_('submit_label')}}</button>
</form>

<ul>
% for number in entered:
    <li>{{_('entered')}}: <b>{{number}}</b> [{{timestamp}}]</li>
  % end
</ul>
</div>
</div>

% include('views/footer.tpl')
