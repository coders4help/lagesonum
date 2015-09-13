<html><head><title>Numbers @ LaGeSo</title></head><body>

<h1>Numbers @ LaGeSo</h1>

<p><a href="/ar_AR">[ Arabian ]</a><a href="/en_US">[ English ]</a><a href="/de_DE">[ Deutsch ]</a></p>

<p>{{_('pitch')}} <em>{{_('wecandoit')}}</em></p>

<form action="/enter" method="post">
   <textarea name="numbers" rows="10" cols="30"></textarea>
   <input type="submit" value="Abschicken">
</form>

<ul>
% for number in entered:
    <li>{{_('entered')}}: <b>{{number}}</b> [{{timestamp}}]</li>
  % end
</ul>

<h3><a href="/query">{{_('searchanumber')}}</a></h3>

<p>Impressum</p>

</body></html>
