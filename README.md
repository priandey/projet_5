# Compare products with Alt'r
AltR is a free command line client which provide you an easy way to find healthy alternative for everyday edible products by browsing the OpenFoodFacts database.
## Firt utilisation
In order to use this program, you will need [MySQL 8.0 to be installed](https://dev.mysql.com/doc/refman/8.0/en/installing.html) on your device.
When MySQL is installed, you can now run the "create_db.sql" as root user to set-up the database of Alt'r.
When first launching the program, be sure to use the following syntax :
```
main.py --fill
```
This will download the dataset and populate the database.

If you have an error while populating the database, you don't have to download again the dataset, you can resolve your MySQL problem, and run the program with the `--commitcache` argument.

To personnalize your API request, you can modify the `CONFIG` constant, at the beginning of `main.py`.
You can choose **the scope** ( = How many pages by category do you need, default is 1), **the size of a page** (default is 1000 products), **the api's link** (default is fr.openfoodfacts) and the **basic categories** you want (default are 5 categories from the top of [this list](https://fr.openfoodfacts.org/categories))

## How to...
AltR first displays an two choices, you can either find a new product to replace, or browse your search history.
```
0 -> Chercher un produit
1 -> Parcourir mon historique de recherche
```
### Browse mode
By pressing "0" and hitting enter, you enter the "browse mode". AltR will display numerous category.
```
0. Food based products
1. Beverages
2. Pastry
3. Meals
4. Crackers
5. Vienna bread
6. Salad
...
```
You may choose a category entering the associated number, or go back to main menu by pressing "E" :
```
# Enter a unique number and press enter to browse a category
-> 2
```
A list of products will be displayed :
```
0.  Gnocchis au chèvre et aux épinards (E)
1.  Pizza Ristorante Quattro Formaggi (D)
2.  Four à pierre, authentique pâte à pizza (D)
3.  Ristorante Pizza Mozarella (D)
4.  Pizza chèvre miel noix (D)
5.  La Grandiosa 4 Formaggi (D)
6.  Flammekueche (D)
7.  Crousti Moelleuse originale 3 fromages (D)
8.  1 Galette Complète (Œuf, Emmental, Jambon) (D)
9.  Ristorante Pizza Speciale (D)
...
````
All you have to do is to choose your product from the list, by pressing the corresponding number and hitting enter.
**You can only choose one option**

Once a product is selected, the program will give you the best alternative there is to your product, regarding the nutrition grade.
```
We found Emincés de poulet, tagliatelles complètes et légumes façon wok as a substitute for Flammekueche
The nutrition grade is A while original product grade was D

Buy it at Picard

More information at : https://fr.openfoodfacts.org/produit/3270160726165/eminces-de-poulet-tagliatelles-completes-et-legumes-facon-wok-picard


Press S to save search, or press <Enter> to go to main menu
```
If you want to save your search, you can by pressing "s" and enter. Whatever choice you make, you will be redirected to the initial choice.

### History mode
By pressing "1" and hitting enter, you enter the "History mode". Your search history will be displayed, from the
most recent search until the oldest.
```
   0.  2019-01-16 07:08:49     | Flammekueche (D) => Emincés de poulet, tagliatelles complètes et légumes façon wok (A)
   1.  2019-01-15 19:41:37     | Choucroute garnie (C) => Le Cassoulet Mitonné (A)
   2.  2019-01-15 19:39:45     | Sushi Box Naniwa (D) => Galettes Orge & Boulghour au chèvre et miel (A)
   3.  2019-01-15 19:39:35     | Lait Concentré Sucré (E) => Yopa (A)
   4.  2019-01-15 19:39:27     | Chocolat Lait extra fin (E) => Pain d\'épices au sirop d\'Agave Jardin Bio (C)
   5.  2019-01-15 19:39:20     | Ice Tea pêche (E) => Coca Cola Zero (B)```
```
By entering the number and pressing enter, you will access to details about your search and the substitute.

### Navigate through search result
On any page, you have the number of pages available :
```
  ...

  Page 1/76            (A/P = 1 | Q/M = 10 | W/N = 100)
```
In order to navigate toward a page, you can either :
- Press A (previous page) or P (next page) to navigate pages 1 by 1.
- Press Q (previous page) or M (next page) to navigate pages 10 by 10.
- Press W (previous page) or W (next page) to navigate pages 100 by 100.
