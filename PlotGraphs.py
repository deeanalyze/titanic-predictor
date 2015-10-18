# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
def PlotGraphs(df):
    fig = plt.figure(figsize=(18,6), dpi=1600) 
    alpha=alpha_scatterplot = 0.2 
    alpha_bar_chart = 0.55
    
    # lets us plot many diffrent shaped graphs together 
    ax1 = plt.subplot2grid((2,3),(0,0))
    # plots a bar graph of those who surived vs those who did not.               
    df.Survived.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
    # this nicely sets the margins in matplotlib to deal with a recent bug 1.3.1
    ax1.set_xlim(-1, 2)
    # puts a title on our graph
    plt.title("Distribution of Survival, (1 = Survived)")    
    
    plt.subplot2grid((2,3),(0,1))
    plt.scatter(df.Survived, df.Age, alpha=alpha_scatterplot)
    # sets the y axis lable
    plt.ylabel("Age")
    # formats the grid line style of our graphs                          
    plt.grid(b=True, which='major', axis='y')  
    plt.title("Survial by Age,  (1 = Survived)")
    
    ax3 = plt.subplot2grid((2,3),(0,2))
    df.Pclass.value_counts().plot(kind="barh", alpha=alpha_bar_chart)
    ax3.set_ylim(-1, len(df.Pclass.value_counts()))
    plt.title("Class Distribution")
    
    plt.subplot2grid((2,3),(1,0), colspan=2)
    # plots a kernel desnsity estimate of the subset of the 1st class passanges's age
    df.Age[df.Pclass == 1].plot(kind='kde')    
    df.Age[df.Pclass == 2].plot(kind='kde')
    df.Age[df.Pclass == 3].plot(kind='kde')
     # plots an axis lable
    plt.xlabel("Age")    
    plt.title("Age Distribution within classes")
    # sets our legend for our graph.
    plt.legend(('1st Class', '2nd Class','3rd Class'),loc='best') 
    
    ax5 = plt.subplot2grid((2,3),(1,2))
    df.Embarked.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
    ax5.set_xlim(-1, len(df.Embarked.value_counts()))
    # specifies the parameters of our graphs
    plt.title("Passengers per boarding location")
    
    
    plt.figure(figsize=(6,4))
    fig, ax = plt.subplots()
    df.Survived.value_counts().plot(kind='barh', color="blue", alpha=.65)
    ax.set_ylim(-1, len(df.Survived.value_counts())) 
    plt.title("Survival Breakdown (1 = Survived, 0 = Died)")
    
    
    fig = plt.figure(figsize=(18,6))

    # create a plot of two subsets, male and female, of the survived variable.
    # After we do that we call value_counts() so it can be easily plotted as a bar graph. 
    # 'barh' is just a horizontal bar graph
    ax1 = fig.add_subplot(121)
    df.Survived[df.Sex == 'male'].value_counts().plot(kind='barh',label='Male')
    df.Survived[df.Sex == 'female'].value_counts().plot(kind='barh', color='#FA2379',label='Female')
    ax1.set_ylim(-1, 2) 
    plt.title("Who Survived? with respect to Gender, (raw value counts) "); plt.legend(loc='best')
    
    
    # adjust graph to display the proportions of survival by gender
    ax2 = fig.add_subplot(122)
    (df.Survived[df.Sex == 'male'].value_counts()/float(df.Sex[df.Sex == 'male'].size)).plot(kind='barh',label='Male')  
    (df.Survived[df.Sex == 'female'].value_counts()/float(df.Sex[df.Sex == 'female'].size)).plot(kind='barh', color='#FA2379',label='Female')
    ax2.set_ylim(-1, 2)
    plt.title("Who Survived proportionally? with respect to Gender"); plt.legend(loc='best')
    
    
    fig = plt.figure(figsize=(18,4), dpi=1600)
    alpha_level = 0.65
    
    # building on the previous code, here we create an additional subset with in the gender subset 
    # we created for the survived variable. I know, thats a lot of subsets. After we do that we call 
    # value_counts() so it it can be easily plotted as a bar graph. this is repeated for each gender 
    # class pair.
    ax1=fig.add_subplot(141)
    female_highclass = df.Survived[df.Sex == 'female'][df.Pclass != 3].value_counts()
    female_highclass.plot(kind='bar', label='female highclass', color='#FA2479', alpha=alpha_level)
    ax1.set_xticklabels(["Survived", "Died"], rotation=0)
    ax1.set_xlim(-1, len(female_highclass))
    plt.title("Who Survived? with respect to Gender and Class"); plt.legend(loc='best')
    
    ax2=fig.add_subplot(142, sharey=ax1)
    female_lowclass = df.Survived[df.Sex == 'female'][df.Pclass == 3].value_counts()
    female_lowclass.plot(kind='bar', label='female, low class', color='pink', alpha=alpha_level)
    ax2.set_xticklabels(["Died","Survived"], rotation=0)
    ax2.set_xlim(-1, len(female_lowclass))
    plt.legend(loc='best')
    
    ax3=fig.add_subplot(143, sharey=ax1)
    male_lowclass = df.Survived[df.Sex == 'male'][df.Pclass == 3].value_counts()
    male_lowclass.plot(kind='bar', label='male, low class',color='lightblue', alpha=alpha_level)
    ax3.set_xticklabels(["Died","Survived"], rotation=0)
    ax3.set_xlim(-1, len(male_lowclass))
    plt.legend(loc='best')
    
    ax4=fig.add_subplot(144, sharey=ax1)
    male_highclass = df.Survived[df.Sex == 'male'][df.Pclass != 3].value_counts()
    male_highclass.plot(kind='bar', label='male highclass', alpha=alpha_level, color='steelblue')
    ax4.set_xticklabels(["Died","Survived"], rotation=0)
    ax4.set_xlim(-1, len(male_highclass))
    plt.legend(loc='best')
    
    
    fig = plt.figure(figsize=(18,12), dpi=1600)
    a = 0.65
    # Step 1
    ax1 = fig.add_subplot(341)
    df.Survived.value_counts().plot(kind='bar', color="blue", alpha=a)
    ax1.set_xlim(-1, len(df.Survived.value_counts()))
    plt.title("Step. 1")
    
    # Step 2
    ax2 = fig.add_subplot(345)
    df.Survived[df.Sex == 'male'].value_counts().plot(kind='bar',label='Male')
    df.Survived[df.Sex == 'female'].value_counts().plot(kind='bar', color='#FA2379',label='Female')
    ax2.set_xlim(-1, 2)
    plt.title("Step. 2 \nWho Survied? with respect to Gender."); plt.legend(loc='best')
    
    ax3 = fig.add_subplot(346)
    (df.Survived[df.Sex == 'male'].value_counts()/float(df.Sex[df.Sex == 'male'].size)).plot(kind='bar',label='Male')
    (df.Survived[df.Sex == 'female'].value_counts()/float(df.Sex[df.Sex == 'female'].size)).plot(kind='bar', color='#FA2379',label='Female')
    ax3.set_xlim(-1,2)
    plt.title("Who Survied proportionally?"); plt.legend(loc='best')
    
    
    # Step 3
    ax4 = fig.add_subplot(349)
    female_highclass = df.Survived[df.Sex == 'female'][df.Pclass != 3].value_counts()
    female_highclass.plot(kind='bar', label='female highclass', color='#FA2479', alpha=a)
    ax4.set_xticklabels(["Survived", "Died"], rotation=0)
    ax4.set_xlim(-1, len(female_highclass))
    plt.title("Who Survived? with respect to Gender and Class"); plt.legend(loc='best')
    
    ax5 = fig.add_subplot(3,4,10, sharey=ax1)
    female_lowclass = df.Survived[df.Sex == 'female'][df.Pclass == 3].value_counts()
    female_lowclass.plot(kind='bar', label='female, low class', color='pink', alpha=a)
    ax5.set_xticklabels(["Died","Survived"], rotation=0)
    ax5.set_xlim(-1, len(female_lowclass))
    plt.legend(loc='best')
    
    ax6 = fig.add_subplot(3,4,11, sharey=ax1)
    male_lowclass = df.Survived[df.Sex == 'male'][df.Pclass == 3].value_counts()
    male_lowclass.plot(kind='bar', label='male, low class',color='lightblue', alpha=a)
    ax6.set_xticklabels(["Died","Survived"], rotation=0)
    ax6.set_xlim(-1, len(male_lowclass))
    plt.legend(loc='best')
    
    ax7 = fig.add_subplot(3,4,12, sharey=ax1)
    male_highclass = df.Survived[df.Sex == 'male'][df.Pclass != 3].value_counts()
    male_highclass.plot(kind='bar', label='male highclass', alpha=a, color='steelblue')
    ax7.set_xticklabels(["Died","Survived"], rotation=0)
    ax7.set_xlim(-1, len(male_highclass))
    plt.legend(loc='best')