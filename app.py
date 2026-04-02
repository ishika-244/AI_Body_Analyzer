import streamlit as st 
import pandas as pd
import joblib
import math


# UI Styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: 
            linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.85)),
            url("https://images.unsplash.com/photo-1571019613914-85f342c6a11e");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Title
st.title("Body Composition Analyzer")
st.caption("Understand your real health beyond just weight.")

with st.expander("How it works"):
 st.markdown("""
              - Body fat is estimated using scientifically validated formulas (US Navy method)
              - Additional health metrics (BMI, visceral fat, muscle mass) are computed using analytical models
              - Machine Learning models are integrated for enhanced predictions where sufficient data is available
              - Results are optimized for interpretability and real-world usability
               """)

# Taking Inputs
st.subheader("📥 Enter Your Body Measurements")
st.caption("Use a measuring tape for accurate results")
colA, colB = st.columns(2)

with colA:
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=15, max_value=80, value=23)
    height = st.number_input("Height (cm)", min_value=120.0, max_value=220.0, value=155.0)
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=150.0, value=44.0)
    gender = st.selectbox("Gender", ["Female", "Male"])

with colB:
    abdomen = st.number_input("Abdomen (cm)", min_value=50.0, max_value=150.0)
    chest = st.number_input("Chest (cm)", min_value=50.0, max_value=150.0)
    hip = st.number_input("Hip (cm)", min_value=60.0, max_value=160.0)
    thigh = st.number_input("Thigh (cm)", min_value=30.0, max_value=100.0)
    neck = st.number_input("Neck (cm)", min_value=25.0, max_value=60.0)

with st.sidebar:
    st.markdown("## 🧠 FitSense AI")

    st.markdown("---")

    st.markdown("### 📌 About")
    st.markdown("""
                 - Hybrid system: formula-based + ML-assisted estimation 
                 - Covers body fat, BMI, visceral fat & muscle metrics  
                 - Built for quick, explainable fitness insights
                """)

    st.markdown("### ⚡ Tips")
    st.markdown("""
- Use accurate measurements  
- Measure in **cm**  
- Stay relaxed while measuring  
""")

    st.markdown("---")
    st.caption("Built with Python, Streamlit & applied health analytics")

# Functions defining 

# 1- Ideal BMI 

def calculate_bmi(weight , height):
        height_in_meter = height/100
        return weight / (height_in_meter**2)

def bmi_category(bmi):
        if bmi<18.5:
                return "Underweight"
        elif bmi >= 18.5  and bmi < 25:
                return "Healthy Weight"
        elif bmi >= 25 and bmi <30:
                return "Overweight"
        elif bmi >=30 :
                if bmi >=30 and bmi<35:
                        return "Class 1 Obesity"
                if bmi >=35 and bmi<40:
                        return "Class 2 Obesity"
                if bmi>=40:
                        return "Class 3 (Severe Obesity)"
                
def bmi_difference(bmi):
    if bmi < 18.5:
        return f"Difference is {18.5 - bmi:.2f} below ideal BMI"    
    elif 18.5 <= bmi <= 24.9:
        return "Ideal BMI"
    else:
        return f"Difference is {bmi - 24.9:.2f} above ideal BMI"
    
    
# 2- Ideal Weight

def calculate_ideal_weight(height , gender):
       height_in_inches = height/2.54
       if gender == "Female":
             return 49 + 1.7 * (height_in_inches - 60)
    #    Devini Formula
       else:
              return 52 + 1.0 * (height_in_inches - 60)

def weight_diff(weight,ideal_weigth):
       diff = weight - ideal_weigth

       if abs(diff) < 0.5:
              return f"Healthy Weight"
       elif diff<0:
              return f"{abs(diff):.2f} kg below ideal"
       else:
              return f"{diff:.2f} Kg above ideal"  
       

          

# 3 - forumla based -- Ideal Body-Fat% --https://www.calculator.net/body-fat-calculator.html

def calculate_body_fat(gender, height, abdomen, neck, hip=None):
    
    try:
        if gender == "Female":
            if (abdomen + hip - neck) <= 0:
                return "Invalid Inputs"

            bf = (
                495 / (
                    1.29579
                    - 0.35004 * math.log10(abdomen + hip - neck)
                    + 0.22100 * math.log10(height)
                )
            ) - 450

        else:  # Male
            if (abdomen - neck) <= 0:
                return "Invalid Inputs"

            bf = (
                495 / (
                    1.0324
                    - 0.19077 * math.log10(abdomen - neck)
                    + 0.15456 * math.log10(height)
                )
            ) - 450

        return round(bf, 2)

    except:
        return "Invalid Body Measurements"
    
    
#Jackson & Pollock Ideal Body Fat Percentages
def get_ideal_body_fat(age, gender): 
    if gender == "Female":
        if age < 25:
            return 18
        elif age < 35:
            return 20
        elif age < 45:
            return 22
        else:
            return 24
    else:  # Male
        if age < 25:
            return 10
        elif age < 35:
            return 13
        elif age < 45:
            return 16
        else:
            return 18
        

#The American Council on Exercise Body Fat Categorization 
def fat_category(body_fat, gender):
    if gender == "Female":
        if body_fat < 14:
            return "Low"
        elif body_fat <= 24:
            return "Fitness"
        elif body_fat <= 31:
            return "Average"
        else:
            return "High"
    else:  # Male
        if body_fat < 6:
            return "Low"
        elif body_fat <= 17:
            return "Fitness"
        elif body_fat <= 24:
            return "Average"
        else:
            return "High"
        
def fat_difference(body_fat, ideal):
    diff = body_fat - ideal

    if diff < 0:
        return f"{abs(diff):.2f}% below ideal"
    elif diff > 0:
        return f"{diff:.2f}% above ideal"
    else:
        return "Exactly at ideal"
    


# 4-- visceral fat

def calculate_visceral_fat(gender, age, weight, height, waist, thigh , bmi):
    if gender == "Female":
        vis_fat = (2.15 * waist) - (3.63 * thigh) + (1.46 * age) + (6.22 * bmi) - 92.713
    else:
        vis_fat = (6 * waist) - (4.41 * thigh) + (1.19 * age) - 213.65

    vis_fat = round(vis_fat / 10)
    vis_fat = max(1, min(vis_fat, 30))
    vis_fat = max(1, min(vis_fat, 30))
    return vis_fat

def ideal_vis_fat():
     return (1 , 9)
     
def visceral_category(vis_fat):
    if vis_fat <= 9:
        return "Normal"
    elif vis_fat <= 14:
        return "High"
    else:
        return "Very High"
    
def visceral_diff(vis_fat):
    low, high = ideal_vis_fat()

    if vis_fat <= high:
        return "Within healthy range"
    elif vis_fat <= 14:
        return f"{vis_fat - high:.1f} above normal"
    else:
        return f"{vis_fat - high:.1f} far above normal"

    

# 5-- muscle estimate category

def estimate_muscle(weight, body_fat):
    fat_mass = weight * (body_fat / 100)
    lbm = weight - fat_mass

    muscle_mass = lbm * 0.5   
    muscle_percent = (muscle_mass / weight) * 100

    return muscle_percent

def muscle_ideal_range(age, gender):
    if gender == "Female":
        if age < 30:
            return 28.4, 39.8
        elif age < 40:
            return 25.0, 36.2
        elif age < 50:
            return 24.2, 34.2
        elif age < 60:
            return 24.7, 33.5
        else:
            return 22.7, 31.9

    else:  # Male
        if age < 30:
            return 37.9, 46.7
        elif age < 40:
            return 34.1, 44.1
        elif age < 50:
            return 33.1, 41.1
        elif age < 60:
            return 31.7, 38.5
        else:
            return 29.9, 37.7
        

def muscle_category(muscle, age, gender):
    low, high = muscle_ideal_range(age, gender)

    if muscle < low:
        return "Low Muscle Mass"
    elif muscle > high:
        return "High Muscle Mass"
    else:
        return "Ideal Muscle Mass"
    
def muscle_diff(muscle, age, gender):
    low, high = muscle_ideal_range(age, gender)

    if muscle < low:
        return f"{low - muscle:.1f}% below ideal"
    elif muscle > high:
        return f"{muscle - high:.1f}% above ideal"
    else:
        return "Within ideal range"
      
    
# 6-- Body age
def calculate_body_age(age, bmi, body_fat, vis_fat, gender):
    score = 0

    # BMI
    if bmi < 18.5:
        score += 1   # underweight = bad
    elif bmi > 25:
        score += 1   # overweight = bad
    # ideal → 0

    # BODY FAT
    if gender == "Female":
        if body_fat < 18:
            score += 1   # too low = bad
        elif 21 <= body_fat <= 33:
            score += 0   # ideal
        else:
            score += 1   # too high = bad

    else:
        if body_fat < 10:
            score += 1
        elif 10 <= body_fat <= 25:
            score += 0
        else:
            score += 1

    # VISCERAL FAT (yaha tumhara rule valid hai)
    if vis_fat <= 5:
        score -= 1   # good → reduce age
    elif vis_fat <= 9:
        score += 0   # normal
    elif vis_fat <= 14:
        score += 1
    else:
        score += 2

    return age + score

def body_age_category(real_age, body_age):
    diff = body_age - real_age

    if diff <= -2:
        return "Younger than your age"
    elif diff <= 2:
        return "Normal"
    else:
        return "Older than your age"
    
def body_age_diff(real_age, body_age):
    diff = body_age - real_age

    if diff == 0:
        return "Same as your actual age"
    elif diff < 0:
        return f"{abs(diff)} years younger"
    else:
        return f"{diff} years older"       

def body_age_message(real_age, body_age):
    if body_age < real_age:
        return "Excellent — your body age is lower than your actual age."
    elif body_age == real_age:
        return "Good — your body age matches your actual age."
    else:
        return "Needs attention — your body age is higher than your actual age."
    
# User Getting Results with button                
if st.button("🚀 Analyze Body"):
    if name.strip() == "":
                 st.warning("Please enter your name")
    elif age < 15:
                 st.warning("This tool is for users above 15")
    else:       
        bmi = calculate_bmi(weight , height)
        category = bmi_category(bmi)
        diff = bmi_difference(bmi)
       
        ideal_weight = calculate_ideal_weight(height , gender)
        w_diff = weight_diff(weight , ideal_weight)

    #    # ml model used for body fat

    #     scaler = joblib.load("models/scaler.pkl")
    #     model = joblib.load("models/fat_model.pkl")

    #     input_data= [[age, weight, height ,abdomen, chest, hip, thigh, neck]]
    #     input_scaled = scaler.transform(input_data)


    #     body_fat= calculate_body_fat(gender,height,abdomen,neck,hip)

    #     body_fat = model.predict(input_scaled)[0]

    # Formula Based Body Fat 
        body_fat = calculate_body_fat(gender , height , abdomen , neck , hip )  
        if isinstance(body_fat, str):
             st.error(body_fat)
             st.stop()
        ideal_fat = get_ideal_body_fat(age , gender)
        fat_cat = fat_category(body_fat , gender)
        fat_diff = fat_difference(body_fat , ideal_fat)

       # Visceral fat 
        vis_fat =calculate_visceral_fat(gender , age , weight  , height , abdomen , thigh , bmi)
        vis_ideal = ideal_vis_fat()
        vis_cat = visceral_category(vis_fat)
        vis_diff = visceral_diff(vis_fat)

       #  muscles 
        muscle_est = estimate_muscle(weight , body_fat)
        mus_ideal = muscle_ideal_range(age , gender)
        mus_category = muscle_category(muscle_est, age, gender)
        mus_diff = muscle_diff(muscle_est, age , gender)
       
         
       # body age 
        b_age = calculate_body_age(age , bmi , body_fat , vis_fat,gender)
        b_category = body_age_category(age , b_age)
        b_diff = body_age_diff(age , b_age)
        body_age_msg = body_age_message(age, b_age)



        # UI
        
        st.divider()
        st.subheader(f"📊 Your Health Summary, {name}")

        col1, col2, col3 = st.columns(3)

        with col1:
         st.metric("BMI", f"{bmi:.2f}", diff)

        with col2:
          st.metric("Body Fat %", f"{body_fat:.2f}%", fat_diff)

        with col3:
         st.metric("Weight", f"{weight:.2f} kg", w_diff)
        
        col4, col5, col6 = st.columns(3)

        with col4:
         st.metric("Visceral Fat", vis_fat, vis_diff)

        with col5:
         st.metric("Muscle Mass %", f"{muscle_est:.2f}%", mus_diff)

        with col6:
         st.metric("Body Age", b_age, b_diff)

        if fat_cat == "Low":
          st.warning("⚠️ Low body fat – focus on strength training & nutrition.")
        elif fat_cat == "High":
         st.warning("⚠️ High body fat – consider fat loss strategies.")
        elif fat_cat in ["Fitness", "Average"]:
         st.success("✅ Healthy body fat range.")
        

       


        st.markdown("### 🧠 Final Verdict")

        st.write(f"""
                 - Your BMI indicates: **{category}**
                 - Body fat is **{fat_cat}**
                 - Muscle condition: **{mus_category}**
                 - Body age status: **{body_age_msg}**
                 """)
        # data = {
        #        "Metric" : ["BMI" , "Weight" , "Body Fat%" , "Visceral Fat%" , "Muscle Mass" , "Body Age"],
        #        "Actual" : [f"{bmi:.2f}" , f"{weight:.2f} kg",f"{body_fat:.2f}%",vis_fat , f"{muscle_est:.2f}" , f"{b_age:.2f}"],
        #        "Ideal" : [f"18.5 - 24.9" , f"{ideal_weight:.2f}kg",f"{ideal_fat}" , 5 , f"{mus_ideal}+%" ,f"{age}"],
        #        "category":[category , category , fat_category , vis_cat , mus_category ,b_category ],
        #        "Difference":[diff , w_diff , fat_diff, vis_diff , mus_diff , b_diff]
        # }

        # df = pd.DataFrame(data)
        # df = df.set_index("Metric")

        # st.dataframe(df) 

st.caption("Estimates are based on formulas and may differ from medical devices (e.g., BIA scans).")