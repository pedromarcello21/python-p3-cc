class Article:
    articles = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.articles.append(self)
    def __repr__(self):
        return f"Article(author={self.author}, magazine={self.magazine}, title={self.title})"


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author (self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("author must be of type Author")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine (self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise Exception("magazine must be of type Magazine")
            
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50 and not hasattr(self, "_title"):
            self._title = value
        else:
            raise Exception("Title must be a string greater than 5 and less than 50 inclusive")
        
class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Author(name={self.name})"

    def articles(self):
        return[article.title for article in Article.articles if article.author == self]
        

    def magazines(self):
        return list(set([article.magazine for article in Article.articles if article.author == self]))

    def add_article(self, magazine, title):
        ##Article is author, magazine, title
        ##magazine is name and category
        ##would have to make magazine instance?
        return Article(self, magazine, title)

        

    def topic_areas(self):
        return list(set([article.magazine.category for article in Article.articles if article.author == self]))
        

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, '_name'):
            self._name = value
        else:
            raise Exception("name must be a string value greater than 0")



class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    def __repr__(self):
        return f"Magazine(name={self.name}, category={self.category})"

    def articles(self):
        return [article for article in Article.articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in Article.articles if article.magazine == self))

    def article_titles(self):
        if len(Article.articles)>0:
            return [article.title for article in Article.articles if article.magazine == self]
        else:
            return None
        

    def contributing_authors(self):
        authors = list(set(article.author for article in Article.articles if article.magazine == self))
        contributing_authors = []
        for author in authors:
            if len([article for article in Article.articles if article.magazine == self and article.author == author]) > 2:
                contributing_authors.append(author)
        if len(contributing_authors) > 0:
            return contributing_authors
        else:
            return None

    def top_publisher(self):
        articles = list(article.author.name for article in Article.articles if article.magazine == self)
        return max(articles)
                

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):

        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise Exception("Name must be a string greater than 2 character and less than 16 characters inclusive")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):

        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise Exception("Category must be a string greater than 0")