#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Creating Authors
    author1 = Author("Pedro")
    author2 = Author("Tay")
    author3 = Author("mini")
    author4 = Author("andrew")
    author5 = Author("sasha")

    # Creating Magazines
    magazine1 = Magazine("Conde", "Fly")
    magazine2 = Magazine("MM", "Super Fly")
    magazine3 = Magazine("Prada", "Fashion")
    magazine4 = Magazine("Tech Today", "Technology")
    magazine5 = Magazine("Foodie", "Culinary")

    # Creating Articles
    article1 = Article(author1, magazine1, "The December Issue")
    article2 = Article(author2, magazine2, "October Festivities")
    article3 = Article(author2, magazine3, "May Flowers")
    article4 = Article(author2, magazine3, "June Blossoms")
    article5 = Article(author1, magazine3, "November Rain")
    article6 = Article(author3, magazine4, "Tech Innovations")
    article7 = Article(author3, magazine4, "AI in 2024")
    article8 = Article(author4, magazine5, "Gourmet Cooking")
    article9 = Article(author4, magazine5, "Desserts Galore")
    article10 = Article(author5, magazine1, "Travel Tips")

    # Additional Articles for Testing Contributing Authors
    article11 = Article(author1, magazine3, "Winter Wonderland")
    article12 = Article(author1, magazine3, "Spring Awakening")

    # Test some more combinations
    article13 = Article(author5, magazine2, "The New Wave")
    article14 = Article(author5, magazine2, "Autumn Leaves")
    article15 = Article(author5, magazine2, "Summer Breeze")


    
    
    
    # # don't remove this line, it's for debugging!
    ipdb.set_trace()
