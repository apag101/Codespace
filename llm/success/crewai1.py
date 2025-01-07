#Medium article: https://medium.com/towards-data-science/ai-for-bi-building-a-business-information-report-with-crewai-and-openai-d6771dea9dad

import os
os.environ["OPENAI_API_KEY"] = "apikey"

from crewai import Agent, Task, Crew
llm = "gpt-4o-mini"

from crewai_tools import FileReadTool, FileWriterTool

file_read_tool = FileReadTool()
file_writer_tool = FileWriterTool()


# Define agent

chart_agent = Agent(
        role="Chart creator",
        goal="""Read the data provided and create a matplotlib chart from 
                that data.
                If you are given specific instructions on how to draw the 
                chart then follow them, if not then create a chart that 
                best represents the data""",
        backstory="""You aim is to read and analyse sales data and create 
                     a mathplotlib chart""",
        tools=[file_read_tool, file_writer_tool],
        llm=llm,
        allow_code_execution=True
    )

files = [
    {
        'data_file_name':'sales_product_cat.csv',
        'chart_file_name': 'sales_product_summary.png',
    },
    {
        'data_file_name': 'monthly_sales.csv',
        'chart_file_name': 'monthly_sales.png',
    },
    {
        'data_file_name': 'sales_by_region.csv',
        'chart_file_name': 'sales_by_region.png',
    }
]

create_chart = Task(
    description="""Create a chart for {data_file_name} and save it in {chart_file_name}.'
                    """,
    expected_output="""A matplotlib chart""",
    agent=chart_agent,
    tools=[file_read_tool, file_writer_tool]
)

# Define the crew
crew = Crew(
    agents=[chart_agent],
    tasks=[create_chart],
    verbose=True
)
result = crew.kickoff_for_each(inputs=files)

data_analysis_agent = Agent(
        role="Data Analyser",
        goal="""You aim is to read and analyse sales data. You should
                then write a report on sales performance 
                that includes an executive summary.
                """,
        backstory="You are assigned to perform sales analysis for a company",
        tools=[file_read_tool, file_writer_tool],
        llm=llm,
        allow_code_execution=False
    )

write_report = Task(
    description=f"""The following contains a set of data files and
                    corresponding charts:
                        {files}
                    Write report in Markdown that includes and overview of all
                    of the sales data and incorporate the corresponding charts.If the information is available, or you can calculate it,
                    try and answer the following questions: 
                    1. What has been the overall revenue for the latest month?
                    2. What are the top selling 5 items during the reporting 
                    period?
                    3. In which regions have there been the most sales and 
                    what items are popular those regions?
                    4. What sort of growth has there been over the reporting 
                    period?
                    5. Are there any trends that you can detect?
                    The overview of the data and the corresponding charts from {files} should be included in an appendix.
                    
                    Save the result in the file './report.md'.
                    """,
    expected_output="""A markdown file""",
    agent=data_analysis_agent,
    tools=[file_read_tool, file_writer_tool]
)
# Define the crew
crew = Crew(
    agents=[data_analysis_agent],
    tasks=[write_report],
    verbose=True
)
result = crew.kickoff()