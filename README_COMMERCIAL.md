# Autobiography Template - Commercial Version

A beautiful, responsive Django web application for creating and managing personal autobiographies. Perfect for individuals wanting to document their life stories, family historians, or anyone interested in preserving personal memories.

## Features

### 📝 Content Management
- **Chapter Creation**: Write and organize your life story in chapters
- **Rich Text Editor**: TinyMCE integration for advanced text formatting
- **Chapter Ordering**: Arrange chapters in any order you prefer
- **Search Functionality**: Find specific content across all chapters

### 📸 Media Management
- **Photo Gallery**: Upload and organize images
- **Image Integration**: Add photos to your chapters
- **Lightbox Viewing**: Beautiful image viewing experience
- **Chapter Association**: Link photos to specific chapters

### 🎨 User Experience
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Modern UI**: Clean, professional design using W3.CSS
- **User Authentication**: Secure login system
- **Admin Panel**: Easy content management

### 🔧 Technical Features
- **Django Framework**: Robust, secure, and scalable
- **SQLite/PostgreSQL**: Flexible database options
- **Static File Management**: Optimized for production
- **Export Functionality**: Backup your content

## Installation

### Prerequisites
- Python 3.8+
- pip
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd autobiography
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   COMMERCIAL_MODE=True
   SITE_TITLE=My Life Story
   SITE_SUBTITLE=The Story of My Life
   SITE_DESCRIPTION=Welcome to my personal autobiography
   AUTHOR_NAME=Your Name
   AUTHOR_SIGNATURE=Thanks for reading my story, Your Name
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `COMMERCIAL_MODE` | Enable commercial template mode | `False` |
| `SITE_TITLE` | Main site title | `MyStory` |
| `SITE_SUBTITLE` | Site subtitle/header | `The Story of an Ordinary Man...` |
| `SITE_DESCRIPTION` | Site description | `Through the simplicity...` |
| `AUTHOR_NAME` | Author name | `Peter` |
| `AUTHOR_SIGNATURE` | Author signature | `Thanks for sticking around...` |

### Customization

1. **Change Site Title**: Update `SITE_TITLE` in environment variables
2. **Modify Header**: Change `SITE_SUBTITLE` and `SITE_DESCRIPTION`
3. **Update Author Info**: Modify `AUTHOR_NAME` and `AUTHOR_SIGNATURE`
4. **Custom Styling**: Edit `static/css/main.css` for custom colors and styling

## Usage

### For End Users

1. **Login**: Access the admin panel to create your account
2. **Create Chapters**: Start writing your life story chapter by chapter
3. **Upload Photos**: Add images to complement your stories
4. **Organize Content**: Arrange chapters in chronological or thematic order
5. **Share**: Share your autobiography with family and friends

### For Developers

1. **Customize Templates**: Modify templates in `chapters/templates/`
2. **Add Features**: Extend functionality in `chapters/views.py`
3. **Style Changes**: Update CSS in `static/css/main.css`
4. **Database Changes**: Create and run migrations as needed

## Deployment

### Render (Recommended)

1. **Connect Repository**: Link your GitHub repository to Render
2. **Configure Environment**: Set environment variables in Render dashboard
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `gunicorn core.wsgi:application`

### Other Platforms

The application can be deployed on any platform that supports Django:
- Heroku
- DigitalOcean
- AWS
- Google Cloud Platform

## License

This template is available for commercial use. Please ensure you have the appropriate license for all included libraries and frameworks.

## Support

For support and customization requests, please contact the development team.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

---

**Note**: This is a commercial template version. The original personal content has been replaced with sample content and configuration options for easy customization. 