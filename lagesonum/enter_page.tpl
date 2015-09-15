<html><head><title>Numbers @ LaGeSo</title></head><body>

<h1>Numbers @ LaGeSo</h1>
<h3>enter numbers</h3>

<p>Everyone in the queue at LaGeSo: Please enter the currently displayed numbers. This way, people not in front of LaGeSo can check if their number has been called. It will work, if everyone works together! Today you help entering numbers, tomorrow you can profit from others entering numbers. <em>TOGETHER WE CAN DO IT!</em></p>

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
<a href="impressum.html">Kontakt</a>
</body></html>
