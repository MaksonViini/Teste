terraform {
  required_version = "1.1.4"
}

provider "aws" {
  region  = "us-east-1"
  profile = "tf1"
}

resource "aws_s3_bucket" "b" {
  bucket = "criando-bucket-com-terraform-makson"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
    ManagedBy   = "Terraform"
  }
}
