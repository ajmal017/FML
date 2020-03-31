import sys
# gives backend app access to modules in algDev by adding directory to pythonpath
sys.path.insert(1, '../')
import numpy as np
# gonna have to rewrite this once DB structure in place
import algDev.API.dataGatherer as dataGatherer
import algDev.API.indicators as indicators

def getCategoryDescriptionAtDate(asset, date):
    
    assetData = []
    
    if date=='recent':

        if asset == 'stocks':
            assetData = stocksData
        else:
            assetData = bondsData
        
        return getMostRecentAllocation(assetData)
    
        # find most recent date and return distribution across stocks
    
    else:
        
        if asset == 'stocks':
            assetData = stocksData
        else:
            assetData = bondsData
        
        return getAllocationOnDay(assetData, int(date))
        

def getMostRecentAllocation(assetData):
	testSeries = assetData[0]['series']
	maxDay = testSeries[0]['name']
	for entry in testSeries:
		if entry['name'] > maxDay:
			maxDay = entry['name']
	
	return getAllocationOnDay(assetData, maxDay)
        

def getAllocationOnDay(assetData, day):
	allocationOnDay = []

	for asset in assetData:
		tempDict = {}
		assetName = asset['name']
		currentSeries = asset['series']

		for dayValuePair in currentSeries:
			if dayValuePair['name'] == day:
				tempDict['name'] = assetName
				tempDict['value'] = dayValuePair['value']
				break
		allocationOnDay.append(tempDict)

	return allocationOnDay

bondsData = [
    {
        "name": "US Government Bonds",
        "series": [
          {
            "name": 10,
            "value": 40
          },
          {
            "name": 20,
            "value": 30
          },
          {
            "name": 30,
            "value": 30
          },
          {
              "name": 40,
              "value": 40
            },
            {
              "name": 50,
              "value": 50
            },
            {
              "name": 60,
              "value": 60
            }
        ]
      },
    
      {
        "name": "Idk other bonds",
        "series": [
          {
            "name": 10,
            "value": 60
          },
          {
            "name": 20,
            "value": 70
          },
          {
            "name": 30,
            "value": 70
          },
          {
              "name": 40,
              "value": 60
            },
            {
              "name": 50,
              "value": 10
            },
            {
              "name": 60,
              "value": 40
            }
        ]
      }
]

stocksData = [
    {
        "name": "GS",
        "series": [
          {
            "name": 10,
            "value": 10
          },
          {
            "name": 20,
            "value": 20
          },
          {
            "name": 30,
            "value": 30
          },
          {
              "name": 40,
              "value": 40
            },
            {
              "name": 50,
              "value": 50
            },
            {
              "name": 60,
              "value": 40
            }
        ]
      },
    
      {
        "name": "APPL",
        "series": [
          {
            "name": 10,
            "value": 60
          },
          {
            "name": 20,
            "value": 40
          },
          {
            "name": 30,
            "value": 20
          },
          {
              "name": 40,
              "value": 5
            },
            {
              "name": 50,
              "value": 10
            },
            {
              "name": 60,
              "value": 15
            }
        ]
      },
    
      {
        "name": "FUN",
        "series": [
          {
            "name": 10,
            "value": 20
          },
          {
            "name": 20,
            "value": 10
          },
          {
            "name": 30,
            "value": 40
          },
          {
              "name": 40,
              "value": 27
            },
            {
              "name": 50,
              "value": 25
            },
            {
              "name": 60,
              "value": 25
            }
        ]
      },
  
      {
          "name": "PZZA",
          "series": [
              {
                "name": 10,
                "value": 10
              },
              {
                "name": 20,
                "value": 30
              },
              {
                "name": 30,
                "value": 10
              },
              {
                  "name": 40,
                  "value": 28
                },
                {
                  "name": 50,
                  "value": 15
                },
                {
                  "name": 60,
                  "value": 20
                }
            ]
        }
]

usGovtBondsData = [
          {
            "name": 10,
            "value": 10
          },
          {
            "name": 20,
            "value": 11
          },
          {
            "name": 30,
            "value": 12
          },
          {
              "name": 40,
              "value": 13
            },
            {
              "name": 50,
              "value": 14
            },
            {
              "name": 60,
              "value": 15
            }
        ]

idkOtherBondsData = [
          {
            "name": 10,
            "value": 20
          },
          {
            "name": 20,
            "value": 21
          },
          {
            "name": 30,
            "value": 22
          },
          {
              "name": 40,
              "value": 23
            },
            {
              "name": 50,
              "value": 24
            },
            {
              "name": 60,
              "value": 25
            }
        ]

gsData = [{
            "name": 10,
            "value": 237.75
          },
          {
            "name": 20,
            "value": 239.01
          },
          {
            "name": 30,
            "value": 241.94
          },
          {
              "name": 40,
              "value": 244.30
            },
            {
              "name": 50,
              "value": 241.82
            },
            {
              "name": 60,
              "value": 238
            }]

applData = [
          {
            "name": 10,
            "value": 308.66
          },
          {
            "name": 20,
            "value": 318.85
          },
          {
            "name": 30,
            "value": 321.45
          },
          {
              "name": 40,
              "value": 325.21
            },
            {
              "name": 50,
              "value": 320.03
            },
            {
              "name": 60,
              "value": 321.55
            }
        ]
pzzaData = [
              {
                "name": 10,
                "value": 64.22
              },
              {
                "name": 20,
                "value": 64.74
              },
              {
                "name": 30,
                "value": 64.55
              },
              {
                  "name": 40,
                  "value": 65.75
                },
                {
                  "name": 50,
                  "value": 64.64
                },
                {
                  "name": 60,
                  "value": 64.79
                }
            ]
funData = [
          {
            "name": 10,
            "value": 53.2
          },
          {
            "name": 20,
            "value": 55.21
          },
          {
            "name": 30,
            "value": 53.91
          },
          {
              "name": 40,
              "value": 54.44
            },
            {
              "name": 50,
              "value": 54.52
            },
            {
              "name": 60,
              "value": 54.75
            }
        ]


def getAssetValueOverTime(name):
  if(len(name) < 5):
    return dataGatherer.getPrices(name)
  else:
    return idkOtherBondsData

def getAllAssetNames():
  # THIS IS GONNA NEED TO BE SORTED
  return dataGatherer.getTickers()

def getAllModels():
  # THIS IS GONNA NEED TO BE SORTED
  return ['Model 1', 'Model 2', 'Model 3', 'Model 4', 'Model 5']

multiseriesData = [
      {
        "name": "Stocks",
        "series": [
          {
            "name": 10,
            "value": 10
          },
          {
            "name": 20,
            "value": 20
          },
          {
            "name": 30,
            "value": 30
          },
          {
              "name": 40,
              "value": 40
            },
            {
              "name": 50,
              "value": 50
            },
            {
              "name": 60,
              "value": 40
            }
        ]
      },
    
      {
        "name": "Bonds",
        "series": [
          {
            "name": 10,
            "value": 60
          },
          {
            "name": 20,
            "value": 40
          },
          {
            "name": 30,
            "value": 20
          },
          {
              "name": 40,
              "value": 5
            },
            {
              "name": 50,
              "value": 10
            },
            {
              "name": 60,
              "value": 15
            }
        ]
      },
    
      {
        "name": "Latvian Brothels",
        "series": [
          {
            "name": 10,
            "value": 20
          },
          {
            "name": 20,
            "value": 10
          },
          {
            "name": 30,
            "value": 40
          },
          {
              "name": 40,
              "value": 27
            },
            {
              "name": 50,
              "value": 25
            },
            {
              "name": 60,
              "value": 25
            }
        ]
      },
  
      {
          "name": "Other",
          "series": [
              {
                "name": 10,
                "value": 10
              },
              {
                "name": 20,
                "value": 30
              },
              {
                "name": 30,
                "value": 10
              },
              {
                  "name": 40,
                  "value": 28
                },
                {
                  "name": 50,
                  "value": 15
                },
                {
                  "name": 60,
                  "value": 20
                }
            ]
        }
    ]


indicatorValues = {
  "name": "data", 
  "series": [
      {
        "name": 10,
        "value": 40
      },
      {
        "name": 20,
        "value": 30
      },
      {
        "name": 30,
        "value": 30
      },
      {
          "name": 40,
          "value": 40
        },
        {
          "name": 50,
          "value": 50
        },
        {
          "name": 60,
          "value": 60
        }
    ]}

indicatorDict = {
"SMA": 1,
"EMA": 1,
"Wilder MA": 1,
"MACD": 2,
"MACDSig": 2,
"KST": 0,
"TRIX": 0,
"KSTTrix": 0,
"RSI": 0,
"Prings": 0,
"OLHC": 0,
"Rainbow": "n",
"Oil": 0,
"SNP": 0,
"Reit": 0,
"GOP": 1,
"BOP": 0,
"Volumes": 0,
"Closes": 0,
"UpperBol": 0,
"LowerBol": 0,
"AccumSwing": 0,
"ATR": 1}

modelData = [{'indicator': indicatorName, 'data':[indicatorValues]} for indicatorName in sorted(indicatorDict.keys())]

mockIndicatorData = [
          {
            "name": 0,
            "value": 40
          },
          {
            "name": 4,
            "value": 10
          },
          {
            "name": 8,
            "value": 20
          },
          {
            "name": 12,
            "value": 30
          },
          {
              "name": 16,
              "value": 40
            },
            {
              "name": 20,
              "value": 50
            }
        ]

def getIndicatorData(indicatorName, equity):
  formatted = indicatorName.replace(",", "_")
  print('indicatorName is ', formatted)

  # FOR NOW - JUST USING LENGTH OF HISTORICAL PRICES DATA TO GET LAST X VALUES
  numDays = len(dataGatherer.getPrices('AAPL'))
  test = indicators.get_indicator_value(equity, formatted)
  print('test data looks like', test)
  samples = test[:numDays]
  samples = np.flipud(samples) 
  samples = [item[0] for item in samples] #unpack it

  print('samples', samples )
  data = []

  for i in range(len(samples)):
    data.append({'name': i, 'value': samples[i]}) # reverse the days

  return data