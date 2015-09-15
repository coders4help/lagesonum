<html class="no-js" lang="">
<head>
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <title>Numbers @ LaGeSo</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/normalize/3.0.3/normalize.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
        <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha256-Sk3nkD6mLTMOF0EOpNtsIry+s1CsaqQC1rVLTAy+0yc= sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>

        <style type="text/css">
            .center-block {
                margin: 0 auto;
                max-width: 760px;
            }
            .alert-big {
                text-align: center;
            }
            .alert-big strong {
                font-size: 42px;
            }

        </style>
        <title>LaGeSoNum - showing numbers at LaGeSO in Berlin</title>
    </head>

<body>
<h1>LaGeSoNum - showing numbers at LaGeSO in Berlin</h1>

<p><a href="/ar_AR">[ Arabian ]</a><a href="/en_US">[ English ]</a><a href="/de_DE">[ Deutsch ]</a></p>

<p>{{_('pitch')}} <em>{{_('wecandoit')}}</em></p>

<form action="{{i18n_path('/')}}" method="post">
   <textarea name="numbers" rows="10" cols="30"></textarea>
   <input type="submit" value="Abschicken">
</form>

<ul>
% for number in entered:
    <li>{{_('entered')}}: <b>{{number}}</b> [{{timestamp}}]</li>
  % end
</ul>

<h3><a href="{{i18n_path('/query')}}">{{_('searchanumber')}}</a></h3>

<p><a href="impressum.html">Kontakt</a></p>

</body></html>
