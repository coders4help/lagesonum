<html><head><title>Lagesonum</title></head><body>

<h1>Lagesonum - Nummern eingeben</h1>

<form action="/enter" method="post">
   <textarea name="numbers" rows="10" cols="30"></textarea>
   <input type="submit" value="Abschicken">
</form>

<ul>
% for number in entered:
    <li>eingegeben: <b>{{number}}</b> [{{timestamp}}]</li>
  % end
</ul>

<a href="/">zur Startseite</a>

</body></html>
