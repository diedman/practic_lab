% rebase('layout.tpl', title=title, year=year)

<h2>Create news.</h2>
<h3>{{ message }}</h3>

<form class="form" method="post">
	<label class="form__label">
		Enter title:  <input class="form__input" type="text" name="TITLE"/>
	</label>
	<br>
	<label class="form__label">
		Enter your email: <input class="form__input" type="email" name="EMAIL"/>
	</label>
	<br>
	<label class="form__label">
		Enter your Nick: <input class="form__input" type="tel" name="PHONE"/>
	</label>
	<br>
	<label class="form__label">
		Enter text for new: <textarea class="form__textarea" name="NEW_TEXT"></textarea>
	</label>
	<br>
	<p><input type="submit" value="Create order"></p>
</form>
