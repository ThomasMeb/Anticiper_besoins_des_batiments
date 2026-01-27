#!/bin/bash
# =============================================================================
# Download Seattle Building Energy Benchmarking Dataset from Kaggle
# =============================================================================
#
# Prerequisites:
#   1. Install Kaggle CLI: pip install kaggle
#   2. Configure API credentials:
#      - Go to https://www.kaggle.com/settings
#      - Click "Create New Token" to download kaggle.json
#      - Place it in ~/.kaggle/kaggle.json
#      - chmod 600 ~/.kaggle/kaggle.json
#
# Usage:
#   ./scripts/download_data.sh
#
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Downloading Seattle Building Energy Benchmarking Dataset ===${NC}"

# Check if kaggle CLI is installed
if ! command -v kaggle &> /dev/null; then
    echo -e "${RED}Error: Kaggle CLI is not installed.${NC}"
    echo "Install it with: pip install kaggle"
    exit 1
fi

# Check if credentials are configured
if [ ! -f ~/.kaggle/kaggle.json ]; then
    echo -e "${RED}Error: Kaggle API credentials not found.${NC}"
    echo "1. Go to https://www.kaggle.com/settings"
    echo "2. Click 'Create New Token' to download kaggle.json"
    echo "3. Place it in ~/.kaggle/kaggle.json"
    echo "4. Run: chmod 600 ~/.kaggle/kaggle.json"
    exit 1
fi

# Create data directory if it doesn't exist
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$( dirname "$SCRIPT_DIR" )"
DATA_DIR="$PROJECT_DIR/data"

mkdir -p "$DATA_DIR"

echo -e "${YELLOW}Downloading dataset...${NC}"

# Download the dataset
kaggle datasets download -d city-of-seattle/sea-building-energy-benchmarking -p "$DATA_DIR" --unzip

echo -e "${GREEN}✓ Dataset downloaded successfully${NC}"
echo ""

# Rename files to match notebook expectations (underscores instead of dashes)
echo -e "${YELLOW}Renaming files for notebook compatibility...${NC}"
if [ -f "$DATA_DIR/2016-building-energy-benchmarking.csv" ]; then
    mv "$DATA_DIR/2016-building-energy-benchmarking.csv" "$DATA_DIR/2016_Building_Energy_Benchmarking.csv"
fi
if [ -f "$DATA_DIR/2015-building-energy-benchmarking.csv" ]; then
    mv "$DATA_DIR/2015-building-energy-benchmarking.csv" "$DATA_DIR/2015_Building_Energy_Benchmarking.csv"
fi

echo -e "${GREEN}✓ Files ready for notebooks${NC}"
echo ""
echo "Files downloaded:"
ls -la "$DATA_DIR"
