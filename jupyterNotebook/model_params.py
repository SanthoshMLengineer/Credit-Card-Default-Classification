# importing libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.svm  import SVC

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

from catboost import CatBoostClassifier
from xgboost import XGBClassifier

import numpy as np


models_params = {'KNeighbous': {'model_ini': KNeighborsClassifier(),
                                'params': {'leaf_size':list(range(1,50)),
                                           'n_neighbors':list(range(1,30)),
                                           'p':[1,2]
                                          }
                               },
                 'LogisticRegression':{'model_ini': LogisticRegression(),
                                       'params': {'penalty':['l1', 'l2'],
                                                  'C':np.logspace(-4, 4, 20),
                                                  'solver':['liblinear']
                                                  }
                                      },
                 'Decision_tree': {'model_ini': DecisionTreeClassifier(),
                                   'params': {"max_depth": list(range(1,10,2)),
                                              "criterion": ["gini", "entropy"],
                                              "max_features": ['auto', 'sqrt','log2']
                                             }
                                  },
                 'Random_forest': {'model_ini': RandomForestClassifier(),
                                   'params': {'n_estimators': list(range(10,150,10)),
                                              'max_depth': list(range(2,10,2)),
                                              'bootstrap': [True, False]
                                             }
                                  },
                 'gradient_boost': {'model_ini': GradientBoostingClassifier(),
                                    'params': {'learning_rate':[0.05, 0.001, 0.01],
                                               'n_estimators':list(range(10,200,10)),
                                               'max_depth':list(range(2,8,1))
                                              }
                                    },
                  'xgb': {'model_ini': XGBClassifier(),
                          'params': {'learning_rate':[0.05, 0.001, 0.01],
                                     'n_estimators':list(range(10,200,10)),
                                     'max_depth':list(range(2,8,1))
                                    }
                          },
                  'catboost': {'model_ini': CatBoostClassifier(verbose=False),
                               'params': {'n_estimators':list(range(10,200,10)),
                                          'max_depth':list(range(1,8,1))
                                         }
                              }
               }