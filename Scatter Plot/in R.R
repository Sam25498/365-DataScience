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
                                    guides(size = FALSE) + 
                                    labs(color = "Building Type") + 
                                    scale_color_manual(values = wes_palette(name = "Darjeeling1", n = 5)) + 
                                    theme(legend.justification = c(0.01,1),
                                          legend.position = c(0.01,1)) + 
       
