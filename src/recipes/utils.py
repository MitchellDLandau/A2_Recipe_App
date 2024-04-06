import pandas as pd
import matplotlib.pyplot as plt
import base64
from recipes.models import Recipe
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(6, 3))

    if chart_type == '#1':
        data['ingredient_count'] = data['ingredients'].apply(lambda x: len(x.split(',')))
        size = data['ingredient_count']
        labels = data['name']
        plt.bar(labels, size)
    elif chart_type == '#2':
        data['ingredient_count'] = data['ingredients'].apply(lambda x: len(x.split(',')))
        size = data['ingredient_count']
        labels = data['name']
        plt.title('The larger the piece of the pie the more ingredients the recipe has.')
        plt.pie(size, labels=labels, autopct='%1.1f%%', startangle=140)
    elif chart_type == '#3':
        data['ingredient_count'] = data['ingredients'].apply(lambda x: len(x.split(',')))
        size = data['ingredient_count']
        labels = data['name']
        plt.xlabel('Recipe Name')
        plt.ylabel('Number of Ingredients')
        plt.plot(labels, size)
    else:
        print('Unknown chart type')

    plt.tight_layout()
    chart = get_graph()
    return chart
     

def get_recipe_from_id(val):
   recipeName=Recipe.objects.get(id=val)
   return recipeName