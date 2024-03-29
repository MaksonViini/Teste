terraform {
  required_version = "1.1.4"
}

resource "aws_s3_bucket" "b" {
  bucket = "criando-bucket-com-terraform-makson"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
    ManagedBy   = "Terraform"
    Owner       = "Makson"
    UpdateAt    = "2022-01-24"
  }
}
