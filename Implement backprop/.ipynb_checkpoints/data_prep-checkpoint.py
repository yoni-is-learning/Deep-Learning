{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "admissions = pd.read_csv('binary.csv')\n",
    "\n",
    "# Make dummy variables for rank\n",
    "data = pd.concat([admissions, pd.get_dummies(admissions['rank'], prefix='rank')], axis=1)\n",
    "data = data.drop('rank', axis=1)\n",
    "\n",
    "# Standarize features\n",
    "for field in ['gre', 'gpa']:\n",
    "    mean, std = data[field].mean(), data[field].std()\n",
    "    data.loc[:,field] = (data[field]-mean)/std\n",
    "    \n",
    "# Split off random 10% of the data for testing\n",
    "np.random.seed(21)\n",
    "sample = np.random.choice(data.index, size=int(len(data)*0.9), replace=False)\n",
    "data, test_data = data.ix[sample], data.drop(sample)\n",
    "\n",
    "# Split into features and targets\n",
    "features, targets = data.drop('admit', axis=1), data['admit']\n",
    "features_test, targets_test = test_data.drop('admit', axis=1), test_data['admit']"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
