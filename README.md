# NLP methods for Amazon reviews 

Cochennec Solène, Happi Nono Noémie

## Presentation of the project 

The aim of this project is to recalculate a more efficient rate for each product, based on ratings, reviews (sentiment analysis thanks to NLP methods) and  we might include other key features ("comment helpful", "verified" etc). We will focus first on the original business of Amazon which is books selling, and might this analysis to other sectors. 

## Set up 

### Link github to your local computer 

Open a terminal and type:

```
git clone https://github.com/choslo/amazon_reviews.git
```
It will create a folder "amazon_reviews" (where you are in the terminal) 

### Create and manage branches 


- Create a new branch
```
git branch {nom de la banche}
```

- Move to another branch 
```
git checkout BranchName
```

- Create and move to another branch in the same step
```
git checkout -b {Nom_votre_nouvelle_branch}
```

- List the branches already present on the repository (you should see the main branch "master" and the branch "BrancheDim")

```
git branch -a
```

### Edit and push code on your branch (never on Master !)

 - Update your version with the changes that other made

```
git pull  
```

-  Make git understand that you made some changes

```
git add . 
```

- Commit your changes with a comment

```
git commit -m "add a comment here about your changes"
```

- Update the repo

```
git push
```


## Ligne de conduite

Ne JAMAIS travailler sur master directement.

La bonne pratique de travail est la suivante : 

#### Pull master 

Afin d'être a jour avec le travail des autres.

```
git checkout master
git pull
```