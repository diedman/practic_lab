% rebase('layout.tpl', title=title, year=year)

<h2>Create news.</h2>
<h3>{{ message }}</h3>

<form action="/newsAdd" method="post">
	<label class="form__label">
		Enter title:  <p><input class="form__input" type="text" name="TITLE"></p>
	</label>
	<br>
	<label class="form__label">
		Enter your email: <p><input class="form__input" type="email" name="EMAIL"></p>
	</label>
	<br>
	<label class="form__label">
		Enter your Nick: <p><input class="form__input" type="text" name="NICK"></p>
	</label>
	<br>
	<label class="form__label">
		Enter text for new: <p><textarea class="form__textarea" name="NEW_TEXT"></textarea></p>
	</label>
	<br>
	<p><input type="submit" value="Create new"></p>
</form>
