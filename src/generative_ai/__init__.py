def main() -> None:
    print("Hello from generative-ai!")
    class Movie(BaseModel):
    title: str 
    release_year : Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

    const ResumeSchema = new mongoose.Schema({
    userId: {type: mongoose.Schema.Types.ObjectId, ref: "User"},
    title: {type: String, default: 'Untitled Resume'},
    public: { type: Boolean, default: false },
    template: { type: String, default: "classic" },
    accent_color: { type: String, default: "#3B82F6" },
    professional_summary: { type: String, default: '' },
    skills: [{ type: String }],
    personal_info: {
        image: {type: String, default: '' },
        full_name: {type: String, default: '' },
        profession: {type: String, default: '' },
        email: {type: String, default: '' },
        phone: {type: String, default: '' },
        location: {type: String, default: '' },
        linkedin: {type: String, default: '' },
        website: {type: String, default: '' },
    },
    
