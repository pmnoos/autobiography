# LifeStory Platform

A professional, feature-rich Django application for creating, managing, and sharing life stories and autobiographies with chapters, photos, and memories. Perfect for individuals, families, and organizations looking to preserve and share their stories online.

## 🌟 Features

- **Chapter Management**: Create, edit, and organize life story chapters
- **Rich Text Editor**: TinyMCE integration for beautiful content creation
- **Photo Gallery**: Upload and display images with your stories
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Search Functionality**: Find specific content across all chapters
- **Admin Panel**: Easy content management through Django admin
- **Export/Backup**: Download your content as JSON backup
- **User Authentication**: Secure login system for content protection

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/autobiography.git
   cd autobiography
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   ```

6. **Set up default login credentials (optional)**
   ```bash
   python manage.py setup_default_user
   ```
   This creates a demo account with username: `demo`, password: `demo123`

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📖 How to Use

### For Demo/Showcase Purposes

1. **Add sample content** (optional):
   ```bash
   python manage.py load_sample_content
   ```
   This creates 5 sample chapters to showcase the app's capabilities.

2. **Set up default login** (optional):
   ```bash
   python manage.py setup_default_user
   ```
   This creates a demo account (username: `demo`, password: `demo123`) for easy access.

3. **Customize the site**:
   - Edit `core/context_processors.py` to change the site title, subtitle, and branding
   - Update the footer information in `templates/base.html`
   - Modify sample content through the admin panel

### For Commercial Use

1. **Set up your platform**:
   - Create a superuser account for administration
   - Configure your site branding in `core/context_processors.py`
   - Set up your domain and hosting environment

2. **Create sample content**:
   - Log in to the admin panel
   - Go to "Chapters" → "Add Chapter"
   - Fill in the title, subtitle, and content
   - Use the rich text editor for formatting

3. **Add photos to your gallery**:
   - Go to "Gallery images" → "Add Gallery Image"
   - Upload images and add descriptions
   - Link images to specific chapters if desired

4. **Organize your content**:
   - Use the "Order" field to arrange chapters chronologically
   - Add meaningful slugs for better URLs
   - Include professional photos and content

## 🌐 Deployment Options

### Option 1: Render (Recommended for beginners)

1. **Create a Render account** at https://render.com
2. **Connect your GitHub repository**
3. **Create a new Web Service**
4. **Configure the service**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn core.wsgi:application`
   - Environment: Python 3

### Option 2: Heroku

1. **Install Heroku CLI**
2. **Create a new Heroku app**
3. **Add PostgreSQL addon**
4. **Deploy using Git**:
   ```bash
   heroku create your-autobiography-app
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Option 3: DigitalOcean App Platform

1. **Create a DigitalOcean account**
2. **Connect your GitHub repository**
3. **Choose Python as the environment**
4. **Configure environment variables**

### Option 4: VPS (Advanced)

1. **Set up a VPS** (Ubuntu recommended)
2. **Install Nginx, Gunicorn, and PostgreSQL**
3. **Configure SSL with Let's Encrypt**
4. **Set up automatic deployments**

## 🔧 Configuration

### Environment Variables

Create a `.env` file in your project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url
```

### Customization

- **Site Title/Subtitle**: Edit `chapters/templates/base.html`
- **Color Scheme**: Modify `static/css/main.css`
- **Sample Content**: Use the management command or edit through admin
- **Logo/Images**: Replace images in `static/images/`

## 📱 Mobile Responsiveness

The app is fully responsive and works great on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🔒 Security Features

- User authentication required for content creation
- CSRF protection enabled
- Secure file upload handling
- Admin panel access control
- SQL injection protection

## 📊 Content Management

### Admin Panel Features
- Create, edit, and delete chapters
- Upload and manage gallery images
- User management
- Content backup and export
- Rich text editing with TinyMCE

### Content Organization
- Chapters ordered by sequence
- Image galleries with descriptions
- Search functionality across all content
- Pagination for large content collections

## 🎨 Customization Guide

### Changing the Theme
1. Edit `static/css/main.css` for colors and styling
2. Modify `chapters/templates/base.html` for layout changes
3. Update header and footer content

### Adding New Features
1. Create new Django apps for additional functionality
2. Add new models in `models.py`
3. Create corresponding views and templates
4. Update URL patterns

## 📞 Support

For questions or issues:
- Check the Django documentation
- Review the code comments
- Create an issue on GitHub
- Contact the development team

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with Django framework
- TinyMCE for rich text editing
- W3.CSS for responsive design
- Lightbox2 for image galleries

---

**Start writing your life story today!** 📖✨
