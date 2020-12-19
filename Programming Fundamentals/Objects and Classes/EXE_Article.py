class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content):
        self.content = self.content.replace(self.content, new_content) # или self.content = new_content

    def change_author(self, new_author):
        self.author = self.author.replace(self.author, new_author) # или self.author = new_author

    def rename(self, new_title):
        self.title = self.title.replace(self.title, new_title) # или self.title = new_title

    def __repr__(self):
        return f'{self.title} - {self.content}: {self.author}'


article = Article("some title", "some content", "some author")
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)
