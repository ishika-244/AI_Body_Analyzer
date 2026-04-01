import streamlit as st 
import pandas as pd
import joblib


# UI Styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: 
            linear-gradient(rgba(0,0,0,0.92), rgba(0,0,0,0.95)),
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
st.title("AI Body Analyzer")
st.caption("AI-powered body composition insights")

with st.expander("How it works"):
    st.write("Body fat predicted using ML model. Other metrics are estimated.")

# Taking Inputs
st.subheader("📥 Enter Your Body Measurements")
st.caption("Use a measuring tape for accurate results")
colA, colB = st.columns(2)

with colA:
    name = st.text_input("Name")
    age = st.number_input("Age", step=1)
    height = st.number_input("Height (cm)")
    weight = st.number_input("Weight (kg)")
    gender = st.selectbox("Gender", ["Female", "Male"])

with colB:
    abdomen = st.number_input("Abdomen (cm)")
    chest = st.number_input("Chest (cm)")
    hip = st.number_input("Hip (cm)")
    thigh = st.number_input("Thigh (cm)")
    neck = st.number_input("Neck (cm)")
with st.sidebar:
    st.markdown("## 🧠 AI Body Analyzer")

    st.markdown("---")

    st.markdown("### 📌 About")
    st.markdown("""
- Predicts **Body Fat % using ML**
- Estimates health metrics  
- Simple & quick analysis  
""")

    st.markdown("### ⚡ Tips")
    st.markdown("""
- Use accurate measurements  
- Measure in **cm**  
- Stay relaxed while measuring  
""")

    st.markdown("---")
    st.caption("Built with ML + Streamlit")

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

def  calculate_ideal_weight(height , gender):
       height_in_inches = height/2.54
       if gender == "Female":
             return 45.5 + 2.3 * (height_in_inches - 60)
       else:
              return 50 + 2.3 * (height_in_inches - 60)
       
def weight_diff(weight,ideal_weigth):
       diff = weight - ideal_weigth

       if abs(diff) < 0.5:
              return f"Healthy Weight"
       elif diff<0:
              return f"{abs(diff):.2f} kg below ideal"
       else:
              return f"{diff:.2f} Kg above ideal"  
          

# 3 - forumla based -- Ideal Body-Fat%

def calculate_body_fat(gender , bmi , age):
       if gender == "Female":
              return 1.20 * bmi + 0.23 * age - 5.4
       else:
              return 1.20 * bmi + 0.23 * age - 16.2   
        
def ideal_body_fat(gender):
       if gender == "Female":
              low, high = 21 , 33
              return f"{low}--{high}"
       else:
              low , high = 10, 20
              return f"{low}--{high}"

def fat_analysis(body_fat, gender):
    if gender == "Female":
        low, high = 21, 33
    else:
        low, high = 10, 20

    if body_fat < low:
        return "Low", f"{low - body_fat:.2f}% below ideal"
    elif body_fat > high:
        return "High", f"{body_fat - high:.2f}% above ideal"
    else:
        return "Healthy", "Within ideal range"


# 4-- visceral fat
 
def visceral_fat_level(body_fat):
    if body_fat < 20:
        vis = 5
    elif body_fat < 30:
        vis = 9
    else:
        vis = 13
    return vis
    
def vis_fat_analysis(vis):
    low , high = 1,9
    if vis < low:
        return "Low", "Below healthy range"
    elif vis > high:
        return "High", f"{vis - high} above ideal"
    else:
        return "Healthy", "Within ideal range"
    

    

# 5-- muscle estimate category
def muscle_ideal(gender):
      if gender == "Male":
            return 45
      else:
            return 40

def muscle_category(gender, muscle_est):
    if gender == "Male" and muscle_est < 45:
        return "Low"
    elif gender == "Female" and muscle_est < 40:
        return "Low"
    else:
        return "Ideal Muscle Mass"
    
def muscle_diff(muscle_est, mus_ideal):
    diff = muscle_est - mus_ideal

    if abs(diff) < 1:
        return "Ideal"
    elif diff < 0:
        return f"{abs(diff):.2f}% below ideal"
    else:
        return f"{diff:.2f}% above ideal"
      
    
# 6-- Body age
def body_age(age, body_fat):
    if body_fat < 20:
        return age - 2
    elif body_fat > 30:
        return age + 3
    else:
        return age
    
def body_age_category(age,b_age):
      if b_age>age:
            "Body Organs are older than actual age"
      elif b_age == age:
            return "Healthy"
      else:
            "Body Organs underdeveloped or Weak" 

def body_age_diff(age, b_age):
    diff = b_age - age

    if diff == 0:
        return "Perfect"
    elif diff > 0:
        return f"{diff} yrs older"
    else:
        return f"{abs(diff)} yrs younger"       
       
    
# User Getting Results with button                
if st.button("🚀 Analyze Body"):
        bmi = calculate_bmi(weight , height)
        category = bmi_category(bmi)
        diff = bmi_difference(bmi)
       
        ideal_weight = calculate_ideal_weight(height , gender)
        w_diff = weight_diff(weight , ideal_weight)

       # ml model used for body fat
        scaler = joblib.load(r'D:\Projects\Herbalife\AI_Body_Analyzer\models\scaler.pkl')
        model = joblib.load(r'D:\Projects\Herbalife\AI_Body_Analyzer\models\fat_model.pkl')

        input_data= [[age, weight, height ,abdomen, chest, hip, thigh, neck]]
        input_scaled = scaler.transform(input_data)

        body_fat = model.predict(input_scaled)[0]
       #  body_fat = calculate_body_fat(gender , bmi , age) -- formula based 
        ideal_fat = ideal_body_fat(gender)
        fat_category, fat_diff = fat_analysis(body_fat, gender)


       # Visceral fat 
        vis_fat = visceral_fat_level(body_fat)
        vis_cat , vis_diff = vis_fat_analysis(vis_fat)

       #  muscles 
        muscle_est = 100 - body_fat
        mus_ideal = muscle_ideal(gender)
        mus_category = muscle_category(gender, muscle_est)
        mus_diff = muscle_diff(muscle_est,mus_ideal)

       
         
       # body age 
        b_age = body_age(age , body_fat)
        b_category = body_age_category(age , b_age)
        b_diff = body_age_diff(age , b_age)


        # More clean UI
        
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

        if body_fat < 21:
             insight = "⚠️ Low body fat — focus on strength & nutrition"
        elif body_fat > 33:
             insight = "⚠️ High body fat — focus on fat loss"
        else:
                insight = "✅ Healthy body composition"
        st.success(insight)
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

        st.warning("This is an estimate, not medical advice.")