import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

df = pd.read_csv('df.csv')
hotel_counts = pd.read_csv('hotel_booking_counts.csv')
revenue_counts = pd.read_csv('hotel_revenue_by_type.csv')
monthly_cancellations = pd.read_csv('monthly_cancellations.csv')
monthly_data = pd.read_csv('monthly_average_adr.csv')
yearly_cancellations = pd.read_csv('yearly_cancellations.csv')
yearly_adr = pd.read_csv('yearly_average_adr.csv')
nationality_dist = pd.read_csv('nationality_distribution.csv')
channel_dist = pd.read_csv('channel_distribution.csv')
cancellation_rates = pd.read_csv('cancellation_rates_by_room_type.csv')
request_counts = pd.read_csv('special_request_counts.csv')
lead_time_counts = pd.read_csv('lead_time_counts.csv')
meal_counts = pd.read_csv('meal_plan_counts.csv')
merged = pd.read_csv('detailed_cancellation_analysis.csv')
cancellation_rates_lead_time = pd.read_csv('cancellation_rates_by_lead_time.csv')
avg_cancellation_by_channel = pd.read_csv('avg_cancellation_by_channel.csv')
avg_cancellation_by_segment = pd.read_csv('avg_cancellation_by_segment.csv')
avg_stay_by_country = pd.read_csv('avg_stay_by_country.csv')
avg_adr_by_customer_type = pd.read_csv('avg_adr_by_customer_type.csv')
holiday_counts = pd.read_csv('holiday_booking_counts.csv')
holidays_revenue = pd.read_csv('holidays_revenue.csv')
occupancy_by_channel = pd.read_csv('occupancy_by_channel.csv')
avg_adr_by_deposit = pd.read_csv('avg_adr_by_deposit.csv')
results_df = pd.read_csv('hotel_occupancy_metrics.csv')
parking_data = pd.read_csv('parking_requirements.csv')
length_of_stay = pd.read_csv('length_of_stay.csv')
prev_bookings = pd.read_csv('previous_bookings.csv')
repeated_guests = pd.read_csv('repeated_guests.csv')
hotel_counts_monthly = pd.read_csv('hotel_booking_month.csv')
revenue_counts_monthly = pd.read_csv('hotel_revenue_by_month.csv')
average_waiting_df= pd.read_csv('average_waiting.csv')


df.drop('Unnamed: 0', axis=1, inplace= True)
df_sample= df.head(10)


st.set_page_config(layout="wide", page_title="Hotel Booking Analysis")

st.markdown('<h1 style= "text-align:center; color: #4169E1 ;">Hotel Booking Analysis Dashboard</h1>', unsafe_allow_html=True)

# Load data
df = pd.read_csv('df.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)

# Create sidebar filters
st.sidebar.header("📊 Dashboard Filters")

# Hotel type filter
hotel_filter = st.sidebar.multiselect(
    '🏨 Hotel Type',
    options=df['hotel'].unique(),
    default=df['hotel'].unique()
)

# Country filter
country_filter = st.sidebar.multiselect(
    '🌍 Country',
    options=df['country'].unique(),
    default=df['country'].unique()
)

# Distribution channel filter
channel_filter = st.sidebar.multiselect(
    '📡 Distribution Channel',
    options=df['distribution_channel'].unique(),
    default=df['distribution_channel'].unique()
)

# Market segment filter
segment_filter = st.sidebar.multiselect(
    '🎯 Market Segment',
    options=df['market_segment'].unique(),
    default=df['market_segment'].unique()
)

# Room type filter
room_type_filter = st.sidebar.multiselect(
    '🛏️ Room Type',
    options=df['room_type_preference'].unique(),
    default=df['room_type_preference'].unique()
)

# Meal plan filter
meal_filter = st.sidebar.multiselect(
    '🍽️ Meal Plan',
    options=df['meal'].unique(),
    default=df['meal'].unique()
)

# Deposit type filter
deposit_filter = st.sidebar.multiselect(
    '💰 Deposit Type',
    options=df['deposit_type'].unique(),
    default=df['deposit_type'].unique()
)

# Customer type filter
customer_filter = st.sidebar.multiselect(
    '👥 Customer Type',
    options=df['customer_type'].unique(),
    default=df['customer_type'].unique()
)

# Cancellation status filter
cancellation_filter = st.sidebar.multiselect(
    '❌ Cancellation Status',
    options=df['is_canceled'].unique(),
    default=df['is_canceled'].unique()
)

# Month filter
month_filter = st.sidebar.multiselect(
    '📅 Arrival Month',
    options=df['arrival_date_month'].unique(),
    default=df['arrival_date_month'].unique()
)

# Year filter
year_filter = st.sidebar.multiselect(
    '📆 Arrival Year',
    options=df['arrival_date_year'].unique(),
    default=df['arrival_date_year'].unique()
)

# Holiday filter
holiday_filter = st.sidebar.multiselect(
    '🎉 Holiday Status',
    options=df['is_holiday'].unique(),
    default=df['is_holiday'].unique()
)

# Season filter
season_filter = st.sidebar.multiselect(
    '🌤️ Season',
    options=df['season'].unique(),
    default=df['season'].unique()
)

# Lead time category filter
lead_time_filter = st.sidebar.multiselect(
    '⏰ Lead Time Category',
    options=df['lead_time_category'].unique(),
    default=df['lead_time_category'].unique()
)

# Special requests filter
special_requests_filter = st.sidebar.slider(
    '🌟 Special Requests',
    min_value=int(df['total_of_special_requests'].min()),
    max_value=int(df['total_of_special_requests'].max()),
    value=(int(df['total_of_special_requests'].min()), int(df['total_of_special_requests'].max()))
)

# Apply all filters
filtered_df = df[
    (df['hotel'].isin(hotel_filter)) &
    (df['country'].isin(country_filter)) &
    (df['distribution_channel'].isin(channel_filter)) &
    (df['market_segment'].isin(segment_filter)) &
    (df['room_type_preference'].isin(room_type_filter)) &
    (df['meal'].isin(meal_filter)) &
    (df['deposit_type'].isin(deposit_filter)) &
    (df['customer_type'].isin(customer_filter)) &
    (df['is_canceled'].isin(cancellation_filter)) &
    (df['arrival_date_month'].isin(month_filter)) &
    (df['arrival_date_year'].isin(year_filter)) &
    (df['is_holiday'].isin(holiday_filter)) &
    (df['season'].isin(season_filter)) &
    (df['lead_time_category'].isin(lead_time_filter)) &
    (df['total_of_special_requests'] >= special_requests_filter[0]) &
    (df['total_of_special_requests'] <= special_requests_filter[1])
]

# Show filter summary
st.sidebar.markdown(f"**🏨 Hotels:** {', '.join(hotel_filter)}")

# Load pre-computed data files (using filtered data where appropriate)
hotel_counts = filtered_df['hotel'].value_counts().reset_index()
hotel_counts.columns = ['Hotel Type', 'Booking Count']

revenue_counts = filtered_df.groupby('hotel')['adr'].sum().reset_index()
revenue_counts.columns = ['Hotel Type', 'Total Revenue']

monthly_cancellations = filtered_df.groupby('arrival_date_month').agg(cancellations=('is_canceled', 'sum')).reset_index()
monthly_data = filtered_df.groupby('arrival_date_month').agg(adr=('adr', 'mean')).reset_index()
yearly_cancellations = filtered_df.groupby('arrival_date_year').agg(cancellations=('is_canceled', 'sum')).reset_index()
yearly_adr = filtered_df.groupby('arrival_date_year').agg(adr=('adr', 'mean')).reset_index()


# Create tabs
tap1, tap2 = st.tabs(['📈 Univariate Analysis', '📊 Bivariate Analysis'])

with tap1:
    show_sample_data = st.checkbox('Show Sample Data', value=False)
    if show_sample_data:
        st.header('Sample Data')
        st.dataframe(df.head(10), hide_index=True)

    # Key metrics - now with 7 columns (need to adjust layout)
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    # Occupancy Rate
    with col1:
        occupancy_rate = (len(filtered_df[filtered_df['is_canceled'] == 0]) / len(filtered_df)) * 100
        st.markdown(f"""
            <div style="background-color: #D1E7DD; padding: 15px; border-radius: 10px;">
                <h4 style="text-align: center; color: black; margin: 0;">Occupancy Rate</h4>
                <h3 style="text-align: center; color: black; margin: 5px 0;">{occupancy_rate:.1f}%</h3>
            </div>
        """, unsafe_allow_html=True)

    # Parking Required
    with col2:
        parking_required = len(filtered_df[filtered_df['required_car_parking_spaces'] > 0])
        parking_percentage = (parking_required / len(filtered_df)) * 100
        st.markdown(f"""
            <div style="background-color: #FFF3CD; padding: 15px; border-radius: 10px;">
                <h4 style="text-align: center; color: black; margin: 0;">Parking Required</h4>
                <h3 style="text-align: center; color: black; margin: 5px 0;">{parking_percentage:.1f}%</h3>
            </div>
        """, unsafe_allow_html=True)

    # Average Stay Duration
    with col3:
        avg_stay = (filtered_df['stays_in_weekend_nights'] + filtered_df['stays_in_week_nights']).mean()
        st.markdown(f"""
            <div style="background-color: #CFE2F3; padding: 15px; border-radius: 10px;">
                <h4 style="text-align: center; color: black; margin: 0;">Avg Stay Duration</h4>
                <h3 style="text-align: center; color: black; margin: 5px 0;">{avg_stay:.1f} nights</h3>
            </div>
        """, unsafe_allow_html=True)

    # Cancellation Rate
    with col4:
        cancellation_rate = (len(filtered_df[filtered_df['is_canceled'] == 1]) / len(filtered_df)) * 100
        st.markdown(f"""
            <div style="background-color: #F8D7DA; padding: 15px; border-radius: 10px;">
                <h4 style="text-align: center; color: black; margin: 0;">Cancellation Rate</h4>
                <h3 style="text-align: center; color: black; margin: 5px 0;">{cancellation_rate:.1f}%</h3>
            </div>
        """, unsafe_allow_html=True)

    # Average Previous Bookings
    with col5:
        # Check if the column exists, otherwise use 0
        if 'previous_bookings_not_canceled' in filtered_df.columns:
            avg_prev_bookings = filtered_df['previous_bookings_not_canceled'].mean()
        else:
            avg_prev_bookings = 0
        st.markdown(f"""
            <div style="background-color: #E8D5E3; padding: 15px; border-radius: 10px;">
                <h4 style="text-align: center; color: black; margin: 0;">Avg Previous Bookings</h4>
                <h3 style="text-align: center; color: black; margin: 5px 0;">{avg_prev_bookings:.1f}</h3>
            </div>
        """, unsafe_allow_html=True)

    # Repeated Guests
    with col6:
        # Check if the column exists, otherwise use 0
        if 'is_repeated_guest' in filtered_df.columns:
            repeated_guests_count = filtered_df['is_repeated_guest'].sum()
            repeated_guests_percentage = (repeated_guests_count / len(filtered_df)) * 100
        else:
            repeated_guests_percentage = 0
        st.markdown(f"""
            <div style="background-color: #D4EDDA; padding: 15px; border-radius: 10px;">
                <h4 style="text-align: center; color: black; margin: 0;">Repeated Guests</h4>
                <h3 style="text-align: center; color: black; margin: 5px 0;">{repeated_guests_percentage:.1f}%</h3>
            </div>
        """, unsafe_allow_html=True)

    # Average Length of Waiting
    with col7:
        # Check if the column exists, otherwise use 0
        if 'days_in_waiting_list' in filtered_df.columns:
            avg_waiting_days = filtered_df['days_in_waiting_list'].mean()
        else:
            avg_waiting_days = 0
        st.markdown(f"""
            <div style="background-color: #CCE5FF; padding: 15px; border-radius: 10px;">
                <h4 style="text-align: center; color: black; margin: 0;">Avg Waiting Days</h4>
                <h3 style="text-align: center; color: black; margin: 5px 0;">{avg_waiting_days:.1f}</h3>
            </div>
        """, unsafe_allow_html=True)


    # Hotel booking counts
    fig0 = px.bar(
        hotel_counts,
        x='Hotel Type',
        y='Booking Count',
        title='Hotel Booking Counts by Type',
        text='Booking Count',
        color='Hotel Type',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        height=400
    )
    fig0.update_traces(texttemplate='%{text:,}', textposition='outside')
    st.plotly_chart(fig0, use_container_width=True)

    # Revenue by hotel type
    fig00 = px.bar(
        revenue_counts,
        x='Hotel Type',
        y='Total Revenue',
        title='Total Revenue by Hotel Type',
        text='Total Revenue',
        color='Hotel Type',
        color_discrete_sequence=px.colors.qualitative.Prism,
        height=400
    )
    fig00.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
    st.plotly_chart(fig00, use_container_width=True)

    # Time series analysis
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    monthly_cancellations['arrival_date_month'] = pd.Categorical(monthly_cancellations['arrival_date_month'], 
                                                                 categories=month_order, ordered=True)
    monthly_cancellations = monthly_cancellations.sort_values('arrival_date_month')
    
    monthly_data['arrival_date_month'] = pd.Categorical(monthly_data['arrival_date_month'], 
                                                        categories=month_order, ordered=True)
    monthly_data = monthly_data.sort_values('arrival_date_month')

    yearly_cancellations['arrival_date_year'] = yearly_cancellations['arrival_date_year'].astype(str)
    yearly_adr['arrival_date_year'] = yearly_adr['arrival_date_year'].astype(str)

    # Create subplots
    figs = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Cancellations by Month", "Cancellations by Year", 
                       "ADR by Month", "ADR by Year")
    )

    fig1 = px.bar(monthly_cancellations, x='arrival_date_month', y='cancellations')
    figs.add_trace(fig1.data[0], row=1, col=1)

    fig2 = px.bar(yearly_cancellations, x='arrival_date_year', y='cancellations')
    fig2.update_xaxes(tickvals=yearly_cancellations['arrival_date_year'].unique())
    figs.add_trace(fig2.data[0], row=1, col=2)

    fig2 = px.bar(yearly_cancellations, x='arrival_date_year', y='cancellations')
    figs.add_trace(fig2.data[0], row=1, col=2)

    fig3 = px.line(monthly_data, x='arrival_date_month', y='adr', markers=True)
    figs.add_trace(fig3.data[0], row=2, col=1)

    fig4 = px.line(yearly_adr, x='arrival_date_year', y='adr', markers=True)
    fig4.update_xaxes(tickvals=yearly_adr['arrival_date_year'].unique())
    figs.add_trace(fig4.data[0], row=2, col=2)

    figs.update_layout(height=600, showlegend=False)
    st.plotly_chart(figs, use_container_width=True)

    # Nationality distribution
    nationality_dist = filtered_df['country'].value_counts().reset_index().head(15)
    nationality_dist.columns = ['Nationality', 'Count']
    
    fig5 = px.pie(
        nationality_dist,
        values='Count',
        names='Nationality',
        title='Distribution of Guest Nationalities (Top 15)',
        color_discrete_sequence=px.colors.sequential.Cividis,
        height=400
    )
    st.plotly_chart(fig5, use_container_width=True)

    # Channel distribution
    channel_dist = filtered_df['distribution_channel'].value_counts().reset_index()
    channel_dist.columns = ['channel', 'count']
    channel_dist['percentage'] = (channel_dist['count'] / channel_dist['count'].sum()) * 100

    fig6 = px.pie(
        channel_dist,
        values='count',
        names='channel',
        title='Booking Distribution by Channel',
        hover_data=['percentage'],
        hole=0.3,
        color_discrete_sequence=px.colors.sequential.Cividis
    )
    st.plotly_chart(fig6, use_container_width=True)

    # Cancellation rate by room type
    cancellation_rates_room = filtered_df[filtered_df['is_canceled'] == 1].groupby('room_type_preference').agg(
        canceled_bookings=('is_canceled', 'sum')
    ).reset_index()
    cancellation_rates_room['cancellation_rate'] = (cancellation_rates_room['canceled_bookings'] / len(filtered_df)) * 100

    fig7 = px.bar(
        cancellation_rates_room,
        x='room_type_preference',
        y='cancellation_rate',
        title='Cancellation Rate by Room Type',
        text='cancellation_rate',
        color='room_type_preference',
        color_discrete_sequence=px.colors.sequential.Viridis,
        height=400
    )
    fig7.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    st.plotly_chart(fig7, use_container_width=True)

    # Special requests
    request_counts = filtered_df['total_of_special_requests'].value_counts().reset_index()
    request_counts.columns = ['Special Request', 'Count']

    fig8 = px.bar(
        request_counts,
        x='Special Request',
        y='Count',
        title='Number of Guests with Special Requests',
        color='Special Request',
        color_discrete_sequence=px.colors.sequential.Cividis,
        text='Count'
    )
    fig8.update_traces(textposition='outside')
    st.plotly_chart(fig8, use_container_width=True)

    # Lead time distribution
    lead_time_counts = filtered_df['lead_time_category'].value_counts().reset_index()
    lead_time_counts.columns = ['lead_time_category', 'count']
    lead_time_counts['proportion'] = lead_time_counts['count'] / lead_time_counts['count'].sum()

    fig9 = px.bar(
        lead_time_counts,
        x='lead_time_category',
        y='proportion',
        title='Booking Lead Time Category Distribution',
        color='lead_time_category',
        color_discrete_sequence=px.colors.sequential.Cividis,
        text='proportion'
    )
    fig9.update_traces(texttemplate='%{text:.1%}', textposition='outside')
    st.plotly_chart(fig9, use_container_width=True)

    # Meal plan distribution
    meal_counts = filtered_df['meal'].value_counts().reset_index()
    meal_counts.columns = ['meal_plan', 'count']
    meal_counts['percentage'] = round(meal_counts['count'] / meal_counts['count'].sum() * 100, 1)
    meal_counts = meal_counts.sort_values('count', ascending=False)

    fig10 = px.bar(
        meal_counts,
        x='count',
        y='meal_plan',
        title='Distribution of Meal Plan Selections',
        color='meal_plan',
        color_discrete_sequence=px.colors.sequential.Cividis,
        text='percentage'
    )
    fig10.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    st.plotly_chart(fig10, use_container_width=True)
    
    st.title('Boxplot Viewer')
    column = st.selectbox('Select a column to display its boxplot:', filtered_df.columns)
    if pd.api.types.is_numeric_dtype(filtered_df[column]):
        fig22 = px.box(
            filtered_df, 
            y=column,
            title=f'Boxplot of {column}',
        )
        # Display interactive boxplot in Streamlit
        st.plotly_chart(fig22)

    else:
        st.title('Count Plot Viewer')
        fig_count = px.histogram(
            filtered_df,
            x=column,
            title=f'Count of Categories in {column}',
            color=column,
            text_auto=True
        )
        st.plotly_chart(fig_count)
        


    st.title("🏨 Hotel Booking Insights Dashboard")

    show_insights = st.checkbox("Show Key Insights", value=True)

    
    if show_insights:
        st.header("📊 Key Insights Summary")
    
        insights = [
            "1. Peak Season Performance: The resort hotel consistently achieves the highest booking counts and revenue during July and August, which are peak months, but also have higher cancelation rate during this time due to higher adr",
            "2. Average Daily Rate (ADR): In peak season, the resort hotel experiences the highest ADR, with slight variations between holidays and weekends.",
            "3. Cancellation Insights: Room type and special requests do not significantly impact cancellation rates. The distribution channel used for bookings does not affect cancellation rates.",
            "4. Geographic Trends: Portugal and travel agencies/tour operators (TA/TO) show the highest booking rates.",
            "5. Meal Preferences: The most requested meal type among guests is bed and breakfast (BB).",
            "6. August Performance: Both hotels report high booking rates and revenue in August.",
            "7. Lead Time and Cancellations: The city hotel has a long lead time for bookings but also a high cancellation rate of 55.7%. The resort hotel has a shorter lead time of 12.9%, which is favorable.",
            "8. Undefined Categories: Bookings categorized as undefined in both distribution channels and customer types have higher cancellation rates.",
            "9. Direct Distribution Success: The direct distribution channel boasts an impressive occupancy rate of 82%.",
            "10. Refundable Booking Cancellations: In the city hotel, refundable bookings have a higher cancellation rate."
        ]
        
        for insight in insights:
            with st.container():
                st.markdown(f"""
                <div style='font-size: 16px; line-height: 1.6; margin: 15px 0;'>
                    {insight}
                </div>
                """, unsafe_allow_html=True)




with tap2:
    # Monthly hotel booking counts by type
    hotel_counts_monthly = filtered_df.groupby(['hotel', 'arrival_date_month']).size().reset_index(name='Booking Count')
    hotel_counts_monthly.columns = ['Hotel Type', 'Month', 'Booking Count']

    fig10 = px.bar(
        hotel_counts_monthly,
        x='Month',
        y='Booking Count',
        color='Hotel Type',
        title='Monthly Hotel Booking Counts by Type',
        text='Booking Count',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        height=400
    )
    fig10.update_traces(texttemplate='%{text:,}', textposition='outside')
    st.plotly_chart(fig10, use_container_width=True)

    # Monthly revenue by hotel type
    revenue_counts_monthly = filtered_df.groupby(['hotel', 'arrival_date_month'])['adr'].sum().reset_index()
    revenue_counts_monthly.columns = ['Hotel Type', 'Month', 'Total Revenue']

    fig11 = px.bar(
        revenue_counts_monthly,
        x='Month',
        y='Total Revenue',
        color='Hotel Type',
        title='Monthly Total Revenue by Hotel Type',
        text='Total Revenue',
        color_discrete_sequence=px.colors.qualitative.Prism,
        height=400
    )
    fig11.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
    st.plotly_chart(fig11, use_container_width=True)

    # Cancellation rate by lead time and hotel
    cancellation_rates_lead = filtered_df.groupby(['lead_time_category', 'hotel'])['is_canceled'].mean().reset_index()
    cancellation_rates_lead['cancellation_rate'] = cancellation_rates_lead['is_canceled'] * 100

    fig12 = px.scatter(
        cancellation_rates_lead,
        x='lead_time_category',
        y='cancellation_rate',
        size='cancellation_rate',
        color='hotel',
        title='Cancellation Rate by Lead Time Category and Hotel Type',
        labels={'cancellation_rate': 'Cancellation Rate (%)'},
        size_max=40,
        height=400
    )
    st.plotly_chart(fig12, use_container_width=True)

    # Cancellation rate by distribution channel
    avg_cancellation_by_channel = filtered_df.groupby('distribution_channel')['is_canceled'].mean().reset_index()
    avg_cancellation_by_channel['cancellation_rate'] = avg_cancellation_by_channel['is_canceled'] * 100

    fig13 = px.bar(
        avg_cancellation_by_channel,
        x='distribution_channel',
        y='cancellation_rate',
        title='Average Cancellation Rate by Distribution Channel',
        color='distribution_channel',
        text='cancellation_rate',
        height=400
    )
    fig13.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    st.plotly_chart(fig13, use_container_width=True)

    # Cancellation rate by market segment
    avg_cancellation_by_segment = filtered_df.groupby('market_segment')['is_canceled'].mean().reset_index()
    avg_cancellation_by_segment['cancellation_rate'] = avg_cancellation_by_segment['is_canceled'] * 100

    fig14 = px.bar(
        avg_cancellation_by_segment,
        x='market_segment',
        y='cancellation_rate',
        title='Average Cancellation Rate by Market Segment',
        color='market_segment',
        text='cancellation_rate',
        height=400
    )
    fig14.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    st.plotly_chart(fig14, use_container_width=True)

    # Correlation matrix
    numerical_vars = ['total_of_special_requests', 'booking_changes', 'days_in_waiting_list', 'is_canceled', 'adr','lead_time','previous_cancellations']
    corr_matrix = df[numerical_vars].corr()

    fig15 = px.imshow(
        corr_matrix,
        title='Correlation Matrix of Key Variables',
        color_continuous_scale='RdBu_r',
        aspect='auto',
        height=400
    )
    st.plotly_chart(fig15, use_container_width=True)

    # Occupancy rate by distribution channel
    occupancy_by_channel = filtered_df.groupby('distribution_channel').apply(
        lambda x: (len(x[x['is_canceled'] == 0]) / len(x)) * 100
    ).reset_index(name='occupancy_rate')

    overall_occupancy = (len(filtered_df[filtered_df['is_canceled'] == 0]) / len(filtered_df)) * 100

    fig16 = px.bar(
        occupancy_by_channel,
        x='distribution_channel',
        y='occupancy_rate',
        title='Occupancy Rate by Distribution Channel',
        color='distribution_channel',
        text='occupancy_rate',
        height=400
    )
    fig16.add_hline(y=overall_occupancy, line_dash="dot", 
                   annotation_text=f"Overall: {overall_occupancy:.1f}%")
    fig16.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    st.plotly_chart(fig16, use_container_width=True)

    # Average length of stay by country
    filtered_df['length_of_stay'] = filtered_df['stays_in_weekend_nights'] + filtered_df['stays_in_week_nights']
    avg_stay_by_country = filtered_df.groupby('country')['length_of_stay'].mean().reset_index()

    fig17 = px.choropleth(
        avg_stay_by_country,
        locations='country',
        locationmode='country names',
        color='length_of_stay',
        title='Average Length of Stay by Country',
        color_continuous_scale='viridis',
        height=500
    )
    st.plotly_chart(fig17, use_container_width=True)

    # ADR by deposit type and hotel
    avg_adr_by_deposit = filtered_df.groupby(['deposit_type', 'hotel'])['adr'].mean().reset_index()

    fig18 = px.bar(
        avg_adr_by_deposit,
        x='deposit_type',
        y='adr',
        color='hotel',
        title='Average ADR by Deposit Type and Hotel Type',
        barmode='group',
        text='adr',
        height=400
    )
    fig18.update_traces(texttemplate='$%{text:.0f}', textposition='outside')
    st.plotly_chart(fig18, use_container_width=True)

    # ADR by customer type and hotel
    avg_adr_by_customer = filtered_df.groupby(['customer_type', 'hotel'])['adr'].mean().reset_index()

    fig19 = px.bar(
        avg_adr_by_customer,
        x='customer_type',
        y='adr',
        color='hotel',
        title='Average ADR by Customer Type and Hotel Type',
        barmode='group',
        text='adr',
        height=400
    )
    fig19.update_traces(texttemplate='$%{text:.0f}', textposition='outside')
    st.plotly_chart(fig19, use_container_width=True)
    
    if 1 in cancellation_filter and 0 in cancellation_filter:
        booking_status = "Total"  # Both canceled and non-canceled selected
    elif 1 in cancellation_filter:
        booking_status = "Canceled"
    elif 0 in cancellation_filter:
        booking_status = "Booking"
    else:
        booking_status = "Total"

    # Holiday vs non-holiday bookings
    holiday_counts = filtered_df.groupby(
        ['is_holiday', 'arrival_date_month', 'season']).size().reset_index(name='booking_count')

    fig20 = px.bar(
        holiday_counts,
        x='arrival_date_month',
        y='booking_count',
        color='is_holiday',
        facet_col='season',
        title=f'Booking: Holiday vs Non-Holiday ({booking_status} by Month and Season)',
        barmode='group',
        height=400
    )
    st.plotly_chart(fig20, use_container_width=True) 

    # Holiday vs non-holiday revenue
    holidays_revenue = filtered_df.groupby(
        ['is_holiday', 'arrival_date_month', 'season']).agg(revenue=('adr', 'sum')).reset_index()

    fig21 = px.bar(
        holidays_revenue,
        x='arrival_date_month',
        y='revenue',
        color='is_holiday',
        facet_col='season',
        title=f'Revenue: Holiday vs Non-Holiday ({booking_status} by Month and Season)',
        barmode='group',
        height=400
    )
    st.plotly_chart(fig21, use_container_width=True)
    
    
