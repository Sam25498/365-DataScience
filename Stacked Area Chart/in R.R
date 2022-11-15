library("ggplot2")
library("dplyr")
library("reshape2")

df_engine_types <- read.csv("C:/Users/sbyeg/Downloads/stacked_area_chart_data.csv", 
                            header = TRUE,
                            sep = ",")
temp <- select(df_engine_types, -matches("Other"))
new_engine_types <- melt(temp, id.vars = "Year")
new_engine_types

area_chart <- ggplot(new_engine_types, aes(x = Year,
                                           y = value, 
                                           fill = variable)) +
                                      geom_area()  +
                      scale_fill_manual(values = c("#ef2026",
                                                   "#7e2987",
                                                   "#011638")) + theme_classic() + 
                      theme(legend.justification = c(0.01, 1), 
                          legend.position = c(0.01,1))
area_chart
