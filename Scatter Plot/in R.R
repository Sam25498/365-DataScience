library("ggplot2")
library("wesanderson")

df_real_estate <- read.csv("C:/Users/sbyeg/Downloads/scatter_data.csv",
                          header = TRUE,
                          sep = ",")
scatter <- ggplot(df_real_estate,
                  aes(x = Area..ft..,
                      y = Price)) + geom_point(aes(color = factor(Building.Type),
                                                   size = 2),
                                               alpha = 0.4) + 
