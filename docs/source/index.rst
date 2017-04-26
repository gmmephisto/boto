.. _index:

===============================================
boto: A Python interface to Amazon Web Services
===============================================

.. note::

  `Boto3 <https://github.com/boto/boto3>`__, the next version of Boto, is now
  stable and recommended for general use.  It can be used side-by-side with
  Boto in the same project, so it is easy to start using Boto3 in your existing
  projects as well as new projects. Going forward, API updates and all new
  feature work will be focused on Boto3.


An integrated interface to current and future infrastructural services
offered by `Amazon Web Services`_.

Currently, all features work with Python 2.6 and 2.7. Work is under way to
support Python 3.3+ in the same codebase. Modules are being ported one at
a time with the help of the open source community, so please check below
for compatibility with Python 3.3+.

To port a module to Python 3.3+, please view our
:doc:`Contributing Guidelines <contributing>` and the
:doc:`Porting Guide <porting_guide>`. If you would like, you can open an
issue to let others know about your work in progress. Tests **must** pass
on Python 2.6, 2.7, 3.3, and 3.4 for pull requests to be accepted.

.. _Amazon Web Services: http://aws.amazon.com/

Getting Started
---------------

If you've never used ``boto`` before, you should read the
:doc:`Getting Started with Boto <getting_started>` guide to get familiar
with ``boto`` & its usage.

Currently Supported Services
----------------------------

* **Compute**

  * :doc:`Elastic Compute Cloud (EC2) <ec2_tut>` -- (:doc:`API Reference <ref/ec2>`) (Python 3)

* **Monitoring**

  * :doc:`CloudWatch <cloudwatch_tut>` -- (:doc:`API Reference <ref/cloudwatch>`) (Python 3)

* **Networking**

  * :doc:`Virtual Private Cloud (VPC) <vpc_tut>` -- (:doc:`API Reference <ref/vpc>`) (Python 3)

* **Storage**

  * :doc:`Simple Storage Service (S3) <s3_tut>` -- (:doc:`API Reference <ref/s3>`) (Python 3)

Additional Resources
--------------------

.. _Boto Issue Tracker: https://github.com/boto/boto/issues
.. _Boto Source Repository: https://github.com/boto/boto
.. _Boto Twitter: http://twitter.com/pythonboto
.. _IRC channel: http://webchat.freenode.net/?channels=boto
.. _Follow Mitch on Twitter: http://twitter.com/garnaat


Release Notes
-------------

.. toctree::
   :titlesonly:

   releasenotes/v2.46.1


.. toctree::

   getting_started
   ec2_tut
   security_groups
   cloudwatch_tut
   vpc_tut
   s3_tut


Indices and tables
==================

