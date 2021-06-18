% rebase('layout.tpl', title=title, year=year)

%import API

<h1>New products</h1>

<div>
	%news = API.get_all_news()
	%for new in news:
		<div class="new new--preview">
			<h1 class="new__title">{{new['title']}}</h1>
			<time class="new__time">{{new['date']}}</time>
			<p class="new__text new__text--preview">{{new['new_text']}}</p>
			<div class="new__author">{{new['author']}}</div>
			<a href="mailto:{{new['email']}}" class="order__email">{{new['email']}}</a>
		</div>
	%end
</div>
