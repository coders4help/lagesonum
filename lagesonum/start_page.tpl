% include('header.tpl', active='helpus')


<div class="container">
      <div class="starter-template">

<p><!--<a href="/ar_AR">[ Arabian ]</a>!--><a href="/en_US">[ English ]</a><a href="/de_DE">[ Deutsch ]</a></p>

<p>{{_('help_pitch')}}</p>

<form action="{{i18n_path('/')}}" method="post">
   <textarea name="numbers" rows="10" cols="30"></textarea>
   <input type="submit" value="{{_('submit_label')}}">
</form>

<ul>
% for number in entered:
    <li>{{_('entered')}}: <b>{{number}}</b> [{{timestamp}}]</li>
  % end
</ul>

% include('footer.tpl')
