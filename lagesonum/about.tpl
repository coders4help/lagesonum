% include('header.tpl')

<h1>Refugees Welcome!</h1>

<p><!--<a href="/ar_AR">[ Arabian ]</a>!--><a href="/en_US">[ English ]</a><a href="/de_DE">[ Deutsch ]</a></p>

<div class="mainmenu">
<h3><a href="{{i18n_path('/query')}}">{{_('searchanumber_link')}}</a></h3>
<h3><a href="{{i18n_path('/')}}">{{_('helpus_link')}}</a></h3>
<h3><a href="{{i18n_path('/about')}}">{{_('about_link')}}</a></h3>
</div>

<h3>{{_('about_title')}}</h3>

<p>{{_('about_par1')}}</p>
<p>{{_('about_par2')}}</p>

% include('footer.tpl')
