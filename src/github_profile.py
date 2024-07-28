def generate_profile(theme,**kwargs):
    with open(f"themes") as f:
        profile = f.read()
    for key,value in kwargs.items():
        profile = profile.replace(f"{{{key}}}", value)
        
    return profile    