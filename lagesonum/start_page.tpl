% include('header.tpl')

<h1>Refugees Welcome!</h1>

<p><!--<a href="/ar_AR">[ Arabian ]</a>!--><a href="/en_US">[ English ]</a><a href="/de_DE">[ Deutsch ]</a></p>

<div class="mainmenu">
<h3><a href="{{i18n_path('/query')}}">{{_('searchanumber_link')}}</a></h3>
<h3><a href="{{i18n_path('/enter')}}">{{_('helpus_link')}}</a></h3>
<h3><a href="{{i18n_path('/about')}}">{{_('about_link')}}</a></h3>
</div>

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
