% include('views/header.tpl')


<div class="container">
      <div class="starter-template">

<p>Bitte helfen Sie mit, diese Seite aktuell zu erhalten, indem Sie alle Nummern, die auf der Anzeigetafel stehen - oder in absehbarer Zeit dort erscheinen werden - eingeben:</p>

<div>
<form action="{{i18n_path(request.fullpath)}}" method="post">
  <div class="form-group">
    <textarea name="numbers" rows="10" class="form-control" placeholder="z.B. A123  BC34 AX99"></textarea>
  </div>
  <button class="btn btn-primary">Abschicken</button>
</form>
</div>

% if entered:
<div class="para">
Herzlichen Dank! Sie haben die folgenden Wartenummern erfolgreich in die Datenbank eingetragen [{{locale_translate(locale_datetime(timestamp))}}]:
<ul>
% for number in entered:
    <li><b>{{number}}</b></li>
% end
</ul>
</div>
% end
% if nonunique:
<div class="para">
Diese Nummer haben Sie bereits eingetragen:
<ul>
%for number in nonunique:
    <li><b>{{number}}</b></li>
%end
</ul>
</div>
%end

% if failed:
<div class="para">
Die folgenden Nummern konnten nicht gespeichert werden:
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
