% include('views/header.tpl', active='helpus')


<div class="container">
      <div class="starter-template">

<p>{{_(u'Du stehst am LaGeSo? Bitte hilf mit, diese Seite aktuell zu erhalten, indem du alle Nummern, die du auf der Anzeigetafel siehst eingibst (NICHT deine eigene Wartenummer):')}}</p>

<form action="{{i18n_path('/enter')}}" method="post">
  <div class="form-group">
    <textarea name="numbers" rows="10" class="form-control" placeholder="e.g. A123 B123 C123"></textarea>
  </div>
  <button class="btn btn-primary">{{_('Abschicken')}}</button>
</form>

<ul>
% for number in entered:
    <li>{{_('entered')}}: <b>{{number}}</b> [{{timestamp}}]</li>
  % end
</ul>
</div>
</div>

% include('views/footer.tpl')
