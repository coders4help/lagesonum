% include('views/header.tpl')


<div class="container">
      <div class="starter-template">

<p>Bitte helfen Sie mit, diese Seite aktuell zu erhalten, indem Sie alle Nummern, die auf der Anzeigetafel stehen - oder in absehbarer Zeit dort erscheinen werden - eingeben:</p>

<form action="{{i18n_path(request.fullpath)}}" method="post">
  <div class="form-group">
    <textarea name="numbers" rows="10" class="form-control" placeholder="z.B. A123  BC34 AX99"></textarea>
  </div>
  <button class="btn btn-primary">Abschicken</button>
</form>

<ul>
% if entered:
    Herzlichen Dank! Sie haben die folgenden Wartenummern erfolgreich in die Datenbank eingetragen:
    % for number in entered:
    <li> <b>{{number}}</b> [{{timestamp}}]</li>
    % end
% end
</ul>
</div>
</div>

% include('views/footer.tpl')
