#!/bin/bash

# 🍽️ Restaurant AI Bot - Installation Verification Script
# Run this script to verify all files are in place

echo "🍽️  RESTAURANT AI ASSISTANT - VERIFICATION SCRIPT"
echo "=================================================="
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counter
PASS=0
FAIL=0

# Function to check file
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $1"
        ((PASS++))
    else
        echo -e "${RED}✗${NC} $1 (MISSING)"
        ((FAIL++))
    fi
}

# Function to check directory
check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} $1/"
        ((PASS++))
    else
        echo -e "${RED}✗${NC} $1/ (MISSING)"
        ((FAIL++))
    fi
}

echo "📁 CHECKING PROJECT STRUCTURE"
echo "──────────────────────────────"

# Check main files
echo ""
echo "📄 Main Application Files:"
check_file "app.py"
check_file "requirements.txt"
check_file ".env.example"

# Check utility files
echo ""
echo "🔧 Utility Modules:"
check_dir "utils"
check_file "utils/__init__.py"
check_file "utils/ai_helper.py"
check_file "utils/recommender.py"
check_file "utils/memory.py"

# Check data files
echo ""
echo "📊 Data Files:"
check_dir "data"
check_file "data/menu.csv"

# Check assets
echo ""
echo "🎨 Assets & Styling:"
check_dir "assets"
check_file "assets/styles.css"

# Check documentation
echo ""
echo "📚 Documentation:"
check_file "README.md"
check_file "SETUP.md"
check_file "DEPLOYMENT.md"
check_file "QUICKSTART.md"
check_file "PROJECT_SUMMARY.md"

# Check other directories
echo ""
echo "📁 Additional Directories:"
check_dir "screenshots"

# Summary
echo ""
echo "=================================================="
echo "📊 VERIFICATION SUMMARY"
echo "=================================================="
echo -e "${GREEN}Passed: $PASS${NC}"
echo -e "${RED}Failed: $FAIL${NC}"
echo ""

if [ $FAIL -eq 0 ]; then
    echo -e "${GREEN}✓ ALL FILES PRESENT!${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Create virtual environment: python3 -m venv venv"
    echo "2. Activate it: source venv/bin/activate"
    echo "3. Install dependencies: pip install -r requirements.txt"
    echo "4. Setup .env file with your Groq API key"
    echo "5. Run app: streamlit run app.py"
    echo ""
    exit 0
else
    echo -e "${RED}✗ SOME FILES ARE MISSING!${NC}"
    echo ""
    echo "Please regenerate the project with all required files."
    echo ""
    exit 1
fi
