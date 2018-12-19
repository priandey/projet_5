# Compare products with AltR
AltR is a free command line client which provide you an easy way to find healthy alternative for everyday edible products by browsing the OpenFoodFacts database.
## How to...
AltR first displays an two choices, you can either find a new product to replace, or browse your search history.
```
1 -> Browse products
2 -> My search history
```
### 1. Browse mode
By pressing "1" and hitting enter, you enter the "browse mode". AltR will display numerous category.
```
Category :
1. Beverages
2. Pastry
3. Meals
4. Crackers
5. Vienna bread
6. Salad
...
```
You can choose one or more, using following syntax :
```
# Enter a unique number and press enter to browse a category
-> 2
# Enter mulptiples number separated by "," and press enter to refine your browsing
-> 3,4
```
A list of products will be displayed :
```
+----+----------------------------------------------------------------------------------------+
| N° | Product Name                                                                           |
+----+----------------------------------------------------------------------------------------+
| 1  | Bouquets de mâche                                                                      |
| 2  | Southwest Salad                                                                        |
| 3  | New potato, tomato & egg salad                                                         |
| 4  | Orzo Pas Ta Salad                                                                      |
| 5  | Melon Free Salad                                                                       |
| 6  | Oriental Salad                                                                         |  
| 7  | Chicken and Bacon Pasta Salad                                                          |
| 8  | Salad'bistrot la Campagnarde (Les Crudettes)                                           |
| 9  | Salade mexicaine au thon                                                               |
+----+----------------------------------------------------------------------------------------+
```` 
All you have to do is to choose your product from the list, by pressing the corresponding number and hitting enter. 
**You can only choose one option here**

Once a product is selected, the program will give you the best alternative there is to your product, regarding the nutrition grade.
```
Alternative for : Oriental Salad (Nutrition grade : E)

==> Taboulé Bio (nutrition grade : B), findable at Monoprix
Follow this link for more information on this product : https://world.openfoodfacts.org/product/3248654098609

Would you like to save this search for later consulting ? 
Yes(Y) or No (N)
```
If you want to save your search, you can by pressing "y" and enter. Whatever choice you make, you will be redirected to the initial choice.

### 2. History mode
By pressing "2" and hitting enter, you enter the "History mode". Your search history will be displayed, from the
most recent search until the oldest.
```
+----+----------+-----------------------------------+----------------------------------------------+
| N° |Date      |Product Name                       |  Substitute                                  |
+----+----------+-----------------------------------+----------------------------------------------+
| 1  |11-01-2018|Oriental Salad                     | Taboulé Bio                                  |
| 2  |24-12-2017|Southwest Salad                    | Coleslaw                                     |
| 3  |15-12-2017|New potato, tomato & egg salad     | Salade césar                                 |
```
By entering the number and pressing enter, you will access to details about your search and the substitute.
```
Alternative for : Oriental Salad (Nutrition grade : E)
Search date : 11-01-2018

==> Taboulé Bio (nutrition grade : B), findable at Monoprix
Follow this link for more information on this product : https://world.openfoodfacts.org/product/3248654098609

Would you like to keep this search saved ? 
Yes(Y) or No(N)
```
You can delete your saved search if you don't want it anymore by pressing "N" and enter, or keep it stored by pressing "Y" and enter.*
