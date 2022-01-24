variable "aws_region" {
  type        = string
  description = "The AWS region to use"
  default     = "us-east-1"
}

variable "aws_profile" {
  type        = string
  description = "The AWS profile to use"
  default     = "tf1"
}

variable "instance_ami" {
  type        = string
  description = "The AMI to use for the instance"
  default     = "ami-04505e74c0741db8d"
}

variable "instance_type" {
  type        = string
  description = "The instance type to use"
  default     = "t2.micro"
}

variable "instance_tags" {
  type        = map(string)
  description = "The tags to apply to the instance"
  default = {
    Name    = "Ubuntu"
    Project = "Aprendendo Terraform"
  }

}
