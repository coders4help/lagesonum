% include('header.tpl')

<nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <div class="navbar-brand">Refugees Welcome!</div>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="{{i18n_path('/')}}">{{_('helpus_link')}}</a></li>
            <li><a href="{{i18n_path('/query')}}">{{_('searchanumber_link')}}</a></li>
            <li><a href="{{i18n_path('/about')}}">{{_('about_link')}}</a></li>
            <li><a href="{{i18n_path('/impressum')}}">{{_('contact_link')}}</a></li>        
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>


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
